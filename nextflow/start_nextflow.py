#!/usr/bin/env python
import sys
import time
import logging
import os
import json
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler


# for docker test
UPLOADS = "/nextflow_pipeline/uploads"
DOWNLOADS = "/nextflow_pipeline/downloads"
NEXTFLOW_FOLDER = "/nextflow_pipeline/nf-core-clinvap"
NF_CONF = "/nextflow_pipeline/clinvap_conf"
WORK_DIR = "/nextflow_pipeline/work"


class MyHandler(FileSystemEventHandler):


    def on_created(self, event):
        # call nextflow on new vcf file

        # Set custom filename for log file
        name = os.path.basename(event.src_path) + ".log"
        log = os.path.join(DOWNLOADS, name)

        # Get pipeline parameters
        conf = os.path.join(NF_CONF, ".conf.txt")

        for i in range(3):
            try:
                with open(conf, "r") as nf_conf:
                    values = json.load(nf_conf)
                genome_assembly = values["assembly"]
                d_filter = values["filter"]
                icd10 = values["icd10"]
                # Create metadata file, put it in NF_CONF
                metadata = os.path.join(NF_CONF, ".metadata.json")
                with open(metadata, "w") as metadata_file:
                    json.dump({"do_name": "", "doid": "","icd10": icd10}, metadata_file, indent=4)
                break
            except IOError:
                if i !=2:
                    time.sleep(30)
                    continue
                else:
                    sys.exit("Problems in loading arguments")


        try:
            cnv_name = os.path.splitext(os.path.basename(event.src_path))[0] + ".tsv"
            print(cnv_name)
            cnv_path = os.path.join(NF_CONF, cnv_name)
            print(cnv_path)
            if not os.path.isfile(cnv_path):
                clinvap = subprocess.run(
                    ['nextflow', '-log', log, 'run', 'main.nf', '-w', WORK_DIR, '--skip_vep', 'true', '--annotated_vcf', event.src_path, '--metadata_json', metadata, '--diagnosis_filter_option', d_filter, '--genome', genome_assembly, '--outdir', DOWNLOADS, '-profile', 'parameters'], cwd=NEXTFLOW_FOLDER, check=True)
            else:
                print("cnv_exits")
                clinvap = subprocess.run(
                    ['nextflow', '-log', log, 'run', 'main.nf', '-w', WORK_DIR, '--skip_vep', 'true', '--annotated_vcf', event.src_path, '--cnv', cnv_path, '--metadata_json', metadata, '--diagnosis_filter_option', d_filter, '--genome', genome_assembly, '--outdir', DOWNLOADS, '-profile', 'parameters'], cwd=NEXTFLOW_FOLDER, check=True)

            if clinvap.returncode == 0:
                print("Pipeline is finished. Deleting VCF.")
                os.remove(event.src_path)
                os.remove(metadata)
                if os.path.isfile(cnv_path):
                    os.remove(cnv_path)
        except subprocess.CalledProcessError:
            print("Pipeline failed. Deleting VCF")
            os.remove(event.src_path)
            os.remove(metadata)
            if os.path.isfile(cnv_path):
                os.remove(cnv_path)



if __name__ == "__main__":
    # format for logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = UPLOADS

    # initialize event handler
    event_handler = MyHandler()
    # initialize observer
    observer = Observer()
    observer.schedule(
        event_handler, path, recursive=True)
    
    # start observer
    observer.start()

    try:
        while observer.isAlive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

#!/usr/bin/env python
import sys
import time
import logging
import os
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
    
        # # Set custom filename for log file
        name = os.path.basename(event.src_path) + ".log"
        log = os.path.join(DOWNLOADS, name)

        # Get pipeline parameters
        conf = os.path.join(NF_CONF, ".conf.txt")

        for i in range(3):
            try:
                with open(conf, "r") as nf_conf:
                    values = json.load(nf_conf)
                genome_assembly = values["assembly"]
                break
            except IOError:
                if i != 2:
                    time.sleep(30)
                    continue
                else:
                    sys.exit("Problems in loading arguments")
                    

        # call nextflow on new vcf file
        clinvap = subprocess.run(
            ['nextflow', '-log', log, 'run', 'main.nf', '-w', WORK_DIR, '--skip_vep', 'false', '--vcf', event.src_path, '--genome', genome_assembly, '--outdir', DOWNLOADS, '-profile', 'parameters'], cwd=NEXTFLOW_FOLDER)

        # print(event.event_type)
        # print(os.path.abspath(event.src_path))
        # print(app.config["UPLOADS"]) 


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

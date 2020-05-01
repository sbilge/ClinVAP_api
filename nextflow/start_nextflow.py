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

genome_assembly = sys.argv[1]

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # # call nextflow on new vcf file
        # # change the path according to the VMs folder structure etc. 
        clinvap = subprocess.run(
            ['nextflow', 'run', 'main.nf', '--vcf', os.path.abspath(event.src_path), '--genome', genome_assembly, '--outdir', DOWNLOADS, '-profile', 'parameters'], cwd=NEXTFLOW_FOLDER)

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


import sys
import time
import logging
import os
import subprocess
from app import app
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

UPLOAD_DIRECTORY = app.config["UPLOADS"]
DOWNLOAD_DIRECTORY = app.config["DOWNLOADS"]

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # # call nextflow on new vcf file
        # # change the path according to the VMs folder structure etc. 
        cwd_path = "/Volumes/clinical_re/ClinVAP_nf-core/nf_core/nf-core-clinvap"
        clinvap = subprocess.run(
            ['nextflow', 'run', 'main.nf', '--annotated_vcf', os.path.abspath(event.src_path), '--outdir', DOWNLOAD_DIRECTORY, '-profile', 'test,docker'], cwd=cwd_path)

        # print(event.event_type)
        # print(os.path.abspath(event.src_path))
        # print(app.config["UPLOADS"])


if __name__ == "__main__":
    # format for logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = UPLOAD_DIRECTORY

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


# # Directory needs to change according to VMs file-folder structure
# DIR = "/Users/bilges/Desktop/abi_tuebingen/clinical_reporting/ClinVAP_app/app/static/input/uploads"

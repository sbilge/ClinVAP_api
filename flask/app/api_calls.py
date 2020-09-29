from app import app
from flask import Flask, flash, request, redirect, abort, jsonify, send_from_directory, render_template, make_response, Response
from werkzeug.utils import secure_filename
import json
import time
import os


UPLOADS = app.config["UPLOADS"]
DOWNLOADS = app.config["DOWNLOADS"]
EXTENSIONS = app.config["EXTENSIONS"]
NF_CONF = app.config["NF_CONF"]

if not os.path.exists(UPLOADS):
    os.makedirs(UPLOADS)

if not os.path.exists(DOWNLOADS):
    os.makedirs(DOWNLOADS)

if not os.path.exists(NF_CONF):
    os.makedirs(NF_CONF)


def file_extension_check(filename):
    """Function to restric file extensions"""
    if not "." in filename:
        return False
    ext = os.path.splitext(filename)[1].lower().strip(".")
    if ext in EXTENSIONS:
        return True
    else:
        return False


# Get input from the user
# TODO Check and limit filesize
@app.route("/upload-input", methods=["GET", "POST"])
def upload_input():
    """Upload a file."""
    if request.method == "POST":

        assembly = request.form.get("assembly")
        if not assembly:
            assembly = "GRCh37"  # if None, assign default value
        elif assembly not in ["GRCh37", "GRCh38"]:
            return make_response(jsonify({"error": "Assembly version is not valid"}), 422)
        with open(os.path.join(NF_CONF, ".conf.txt"), "w") as conf:
            json.dump({"assembly": assembly}, conf, indent=4)

        if request.files:
            vcf = request.files["vcf"]

            # check whether file has a name
            if vcf.filename == "":
                flash("File must have a name", "warning")
                print("File must have a name")
                return redirect(request.url)

            # Check file extension
            if not file_extension_check(vcf.filename):
                flash("File extension is not allowed", "warning")
                print("File extension is not allowed")
                return redirect(request.url)

            # create a safe filename
            else:
                filename = secure_filename(vcf.filename)
                vcf.save(os.path.join(UPLOADS, filename))
                flash("File is saved", "success")
                print("File is saved")
                return redirect(request.url)
    return render_template("upload_input.html")


# Give status of report generation process to user

@app.route("/results/<filename>/status", methods=["GET"])
def get_status(filename):
    try:
        logfile_path = os.path.join(DOWNLOADS, filename + ".log")
        with open(logfile_path, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            if "ERROR" in lines:
                status = "Failed"
            else:
                status = "Success"
            if "Execution complete -- Goodbye" in last_line:
                status_2 = "Finished"
                status_report = status + ',' + status_2
            else:
                status_2 = "Running"
                status_report = status_2
        return make_response(jsonify({"Status": status_report}), 200)
    except FileNotFoundError:
        return make_response(jsonify({"error": "Log file not found"}), 404)

    return redirect(request.url)

# Give resulting file to the user

@app.route("/results/<path:filename>", methods=["GET"])
def download_result(filename):
    """Download a file."""
    try:
        # tell nginx to server the file and where to find it
        return send_from_directory(DOWNLOADS+"/reports", filename, as_attachment=True)
    except FileNotFoundError:
        return make_response(jsonify({"error": "File not found"}), 404)

    return redirect(request.url)

# Give user the driver gene info


@app.route("/results/<filename>/tables/driver-genes", methods=["GET"])
def get_driver_genes(filename):
    # check whether filename is given
    if filename == "":
        flash("File must have a name", "warning")
        print("File must have a name")
        return redirect(request.url)

    else:
        try:
            # read in json file
            full_path = DOWNLOADS + "/reports/" + filename
            with open(full_path) as j:
                data = json.load(j)
            drivers = data.get("driver_table")
            return make_response(jsonify(drivers), 200)

        except FileNotFoundError:
            return make_response(jsonify({"error": "File not found"}), 404)
            # abort(404)

    return redirect(request.url)

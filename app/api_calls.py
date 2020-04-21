from app import app
from flask import Flask, flash, request, redirect, abort, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import json
import os


UPLOADS = app.config["UPLOADS"]
DOWNLOADS = app.config["DOWNLOADS"]
EXTENSIONS = app.config["EXTENSIONS"]

if not os.path.exists(UPLOADS):
    os.makedirs(UPLOADS)

if not os.path.exists(DOWNLOADS):
    os.makedirs(DOWNLOADS)

# function to restric file extensions
def file_extension_check(filename):
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


# TODO if there is a file not found error, check whether nextflow is still running on that file or not
# Give resulting file to the user

@app.route("/results/<path:filename>", methods=["GET"])
def download_result(filename):
    """Download a file."""
    try:
        return send_from_directory(DOWNLOADS+"/reports", filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


# Give user the driver gene info 
# TODO Read JSON result, parse, give the parts

@app.route("/results/<filename>/tables/driver-genes", methods=["GET"])
def get_driver_genes(filename):
    # check whether filename is given
    if filename == "":
        flash("File must have a name", "warning")
        print("File must have a name")
        return redirect(request.url)

    # create a safe filename
    else:
        try:
            # read in json file
            full_path = DOWNLOADS + "/reports/" + filename + ".json"
            with open(full_path) as j:
                data = json.load(j)
            drivers = data.get("mskdg")
            return jsonify(drivers)

        except FileNotFoundError:
            abort(404)

    return redirect(request.url)
    

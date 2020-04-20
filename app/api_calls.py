from app import app
from flask import Flask, flash, request, redirect, abort, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os



UPLOAD_DIRECTORY = app.config["UPLOADS"]
DOWNLOAD_DIRECTORY = app.config["DOWNLOADS"]
EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# TODO Read JSON result, parse, give the parts


# Give result to the user
@app.route("/results/<filename>", methods=["GET"])
def download_result(filename):
    """Download a file."""
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


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
            input_vcf = request.files["vcf"]
            
            # check whether file has a name 
            if input_vcf.filename == "":
                print("Image must have a name")
                return redirect(request.url)
            
            # Check file extension 
            if not file_extension_check(input_vcf.filename):
                print("That image extension is not allowed ")
                return request.url

            # create a safe filename 
            else:
                filename = secure_filename(input_vcf.filename)
                input_vcf.save(os.path.join(UPLOAD_DIRECTORY, filename))

            print("file is saved")
            return redirect(request.url)
    return render_template("upload_input.html")

from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "change-me")

S3_BUCKET = os.environ.get("S3_BUCKET", "your-s3-bucket-name")
s3 = boto3.client("s3")

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        try:
            s3.upload_fileobj(file, S3_BUCKET, file.filename)
            flash("File uploaded to S3 successfully!")
        except Exception as e:
            flash(f"Upload failed: {e}")
        return redirect(url_for("upload_file"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

from app.main import bp
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import hashlib
import boto3
import os


@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'POST':
        session['details'] = request.form
        print(session['details'])
        return redirect(url_for('main.video_details'))
    return render_template('main/details.html')


@bp.route('/declaration')
def declaration():
    return render_template('main/declaration.html', heading='Declaration')


@bp.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        # TODO: spin up bucket and dump video, details of user
        if 'file-upload-1' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # TODO: limit the kinds of files that can be uploaded
        print(request.form)
        session['hash'] = checksum_md5(request.files['file-upload-1'])
        file = request.files['file-upload-1']
        filename = secure_filename(file.filename)
        s3 = s3_client()
        # s3.create_bucket(
        #     Bucket='test-htp',
        #     CreateBucketConfiguration={
        #         'LocationConstraint': 'eu-west-1'
        #     },
        # )
        s3 = boto3.resource('s3')
        # s3.Bucket('test-htp').upload_file
        return redirect(url_for('main.complete'))
    return render_template('main/video.html', heading="Submit video evidence")


@bp.route('/video-details', methods=['GET', 'POST'])
def video_details():
    if request.method == 'POST':
        session['further-details'] = request.form.getlist('more-detail')
        return redirect(url_for('main.video'))
    return render_template('main/video-details.html')


@bp.route('/complete')
def complete():
    return render_template(
        'main/complete.html',
        hash=session['hash'][0:6] or 'TEST HASH',
        heading='Submission complete'
    )


def checksum_md5(filename):
    md5 = hashlib.md5()
    with filename.stream as f:
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
    return md5.hexdigest()


def s3_client() -> boto3.client:
    return boto3.client('s3', region_name='eu-west-1')



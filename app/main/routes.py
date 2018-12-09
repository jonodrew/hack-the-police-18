from app.main import bp
from flask import render_template, request, redirect, url_for, flash, session
import hashlib


@bp.route('/')
def index():
    return render_template('base.html')


@bp.route('/video', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        print(request.files['file-upload-1'])
        # TODO: spin up bucket and dump video, details of user
        if 'file-upload-1' not in request.files:
            flash('No file part')
            return redirect(request.url)
        print(request.files)
        session['hash'] = checksum_md5(request.files['file-upload-1'])
        return redirect(url_for('main.complete'))
    return render_template('main/video.html', heading="Submit video evidence")


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

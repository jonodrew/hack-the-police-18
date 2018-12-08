from app.main import bp
from flask import render_template, request, redirect, url_for


@bp.route('/')
def hello_world():
    return render_template('base.html')


@bp.route('/video', methods=['GET', 'POST'])
def video():
    print(request.method)
    if request.method == 'POST':
        # TODO: spin up bucket and dump video, details of user
        pass
    return render_template('main/video.html', heading="Submit video evidence")


@bp.route('/complete')
def complete():
    return render_template('main/complete.html', hash='g3ny9d'.upper())



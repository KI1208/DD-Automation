#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, current_app, request, flash,redirect,url_for,render_template, send_from_directory
from werkzeug.utils import secure_filename
from parse_survey import Parse_survey
from procgen import Procgen
from parse_autosupport import Parse_autosupport
from compare import Compare

UPLOAD_FOLDER = 'C:\\Users\\ikedak2\\PycharmProjects\\DD-Automation\\upload\\'
CONFIG_FOLDER = 'C:\\Users\\ikedak2\\PycharmProjects\\DD-Automation\\config\\'
PROC_FOLDER = 'C:\\Users\\ikedak2\\PycharmProjects\\DD-Automation\\proc\\'
AUTOSUPPORT_FOLDER = 'C:\\Users\\ikedak2\\PycharmProjects\\DD-Automation\\autosupport\\'
RESULT_FOLDER = 'C:\\Users\\ikedak2\\PycharmProjects\\DD-Automation\\result\\'
ALLOWED_EXTENSIONS = set(['xlsx', 'json', 'log'])

app = Flask(__name__)
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONFIG_FOLDER'] = CONFIG_FOLDER
app.config['PROC_FOLDER'] = PROC_FOLDER
app.config['AUTOSUPPORT_FOLDER'] = AUTOSUPPORT_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def toppage():
    lstsurvey = os.listdir(UPLOAD_FOLDER)
    lstconfig = os.listdir(CONFIG_FOLDER)
    lstproc = os.listdir(PROC_FOLDER)
    lstautosupport = os.listdir(AUTOSUPPORT_FOLDER)
    lstresult = os.listdir(RESULT_FOLDER)
    return render_template('toppage.html', filelist =lstsurvey, configlist=lstconfig, proclist=lstproc, autosupportlist=lstautosupport, resultlist=lstresult)


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if 'xlsx' in file.filename:
            dir = app.config['UPLOAD_FOLDER']
        elif 'autosupport' in file.filename:
            dir = app.config['AUTOSUPPORT_FOLDER']

        if file.filename == '':
            flash('No Selected File')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(dir, filename))
            flash('File saved successfully.')
            return redirect(url_for('toppage'))


@app.route('/parse_survey', methods=['POST', 'GET'])
def parse_survey():
    filename = request.args.get('filename')
    Parse_survey(os.path.join(app.config['UPLOAD_FOLDER'], filename)).parse_survey()
    flash('Parsing Survey')
    return redirect(url_for('toppage'))


@app.route('/procgen', methods=['POST', 'GET'])
def procgen():
    filename = request.args.get('filename')
    Procgen(os.path.join(app.config['CONFIG_FOLDER'], filename)).procgen()
    flash('Generating Procedure')
    return redirect(url_for('toppage'))

@app.route('/parse_autosupport', methods=['POST', 'GET'])
def parse_autosupport():
    filename = request.args.get('filename')
    Parse_autosupport(os.path.join(app.config['AUTOSUPPORT_FOLDER'], filename)).parse_autosupport()
    flash('Parsing Autosupport')
    return redirect(url_for('toppage'))


@app.route('/compare', methods=['POST', 'GET'])
def compare():
    compared_files = request.form.getlist("choice")
    # print(compared_files)
    table = Compare([os.path.join(CONFIG_FOLDER, compared_files[0]), os.path.join(RESULT_FOLDER, compared_files[1])]).compare()
    flash('Comparing')
    return table


@app.route('/download/<string:filetype>/<string:filename>', methods=['GET'])
def download_file(filetype, filename):
    # filename = request.args.get('filename')
    if filetype == 'proc':
        dir = app.config['PROC_FOLDER']
        downloadtype = 'text/plain'
    elif filetype == 'config':
        dir = app.config['CONFIG_FOLDER']
        downloadtype = 'text/plain'
    elif filetype == 'survey':
        dir = app.config['UPLOAD_FOLDER']
        downloadtype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif filetype == 'autosupport':
        dir = app.config['AUTOSUPPORT_FOLDER']
        downloadtype = 'text/plain'

    flash('Downloading file')
    return send_from_directory(dir, filename, as_attachment=True, mimetype=downloadtype)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
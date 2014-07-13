#!/usr/bin/env python

import logging
from flask import Flask, render_template, url_for, request, redirect
import katalklog

app = Flask(__name__)

@app.route('/')
def index_page():
  return render_template('index.html')

@app.route('/upload',methods=['POST'])
def file_upload():
  read_file = request.files['file_upload']

  if read_file is None:
    return "Empty!"

  data = katalklog.read_data(read_file)

  sorted_dic = katalklog.sorted_dict(data)

  result = ""
  for key in sorted_dic:
      result += "[%s]:%d " % (key, sorted_dic[key])

  return result#render_template('result.html')

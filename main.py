#!/usr/bin/env python

import logging
from flask import Flask, render_template, url_for, request, redirect
import katalklog

app = Flask(__name__)

limit = 20

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

  if len(sorted_dic) > 20:
    result = dict()
    count = 0
    for key in sorted_dic:
      if count == 20:
        break
      result[key] = sorted_dic[key]
      count+=1
    return render_template('result.html',datas=result)
  else:
    return render_template('result.html',datas=sorted_dic)


@app.route('/sample')
def sample_page():
  """
  sample page for test pie chart and jinja2
  """
  arrays = {'Hello':20,'thankyou':10,'GoodNight':5,'Loveyou':40,'no':2}
  return render_template('result.html',datas=arrays)

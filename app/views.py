from flask import render_template
from app import website

@website.route('/')
def index():
  return render_template('index.html')

@website.route('/red')
def index2():
  return render_template('index2.html', title="red")

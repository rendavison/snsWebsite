from flask import render_template
from app import website

@website.route('/')
def index():
  return render_template('index.html')

@website.route('/about.html')
def about():
  return render_template('about.html', title="About Us")

@website.route('/tickets.html')
def tickets():
  return render_template('tickets.html', title="Buy Tickets")

@website.route('/join.html')
def join():
  return render_template('join.html', title="Join Us!")

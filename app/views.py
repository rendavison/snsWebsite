"""
Deines a relationship between relative urls and html files (i.e. WEBSITE/about links to about.html)

get_txt: 
  a helper function which retrieves the text from a file passed as input.
  We use this function to update information on the website, such as subtroupe descriptions
  and announcements without modifying the source html.
"""
from flask import render_template
from app import website
import os

#### Helper functions ####

def get_txt(filename):
  """
  Return the text stored in app/static/txts/filename.txt if it exists. 

  filename should be a string with extension, for example, "npp.txt"
  """
  # replace getcwd with os.path.dirname, and move txts folder to the same folder as views
  complete_path = os.path.join(os.getcwd(), "app", "static", "txts", filename)

  try:
    with open(complete_path, 'r') as text_file:
      raw_text = text_file.read()
  except IOError:
    raw_text = complete_path
  
  return raw_text

#### Website routes ####

@website.route('/')
def index():
  return render_template('index.html', announcements=get_txt("announcements.txt"))

@website.route('/about.html')
def about():
  return render_template('about.html', title="About Us")

@website.route('/tickets.html')
def tickets():
  return render_template('tickets.html', title="Buy Tickets")

@website.route('/subtroupes.html')
def subtroupes():
  # Dynamically update subtroupes.html with: tisbert.txt, npp.txt, workshopping.txt
  return render_template('subtroupes.html', title="SNS Subtroupes", 
      tisbert_text=get_txt("tisbert.txt"), npp_text=get_txt("npp.txt"), 
      workshopping_text=get_txt("workshopping.txt"))

@website.route('/join.html')
def join():
  return render_template('join.html', title="Join Us!")

@website.route('/alumni.html')
def alumni():
  return render_template('alumni.html', title="Alumni")

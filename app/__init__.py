from flask import Flask

website = Flask(__name__)
from app import views

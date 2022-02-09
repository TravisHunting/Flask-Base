#!/usr/bin/env python3
from flask import Flask, render_template #, request, send_from_directory, send_file
#import os

app = Flask(__name__)

#Heroku postgres
#herokudb = os.getenv('DATABASE_URL')#.replace("\"", "")

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/api/scrape', methods=['POST'])
def scrape():
    return {}

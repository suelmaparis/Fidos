import os
from flask import Flask ,render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

from flask import render_template, url_for
from app import app
from .forms import VendorForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/vendor')
def vendor():
    form = VendorForm()
    return render_template('vendor.html', form=form)

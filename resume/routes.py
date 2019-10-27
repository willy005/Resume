from flask import render_template, url_for
from resume import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/interests')
def interests():
    return render_template('interests.html')

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:18:02 2023

@author: mudil
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Tryon')
def Tryon():
    return render_template('Tryon.html')

@app.route('/OurSamples')
def OurSamples():
    return render_template('OurSamples.html')

@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')




if __name__=="__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
    
    
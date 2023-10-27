from flask import Flask,  request, render_template
import os
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit(): 
    first_name = request.form['first_name']
    surname = request.form['surname']
    mail = request.form['mail']
    weight_kg = request.form['weight_kg']
    height_cm = request.form['height_cm']
    
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
import numpy as np
from flask import Flask, request, render_template, flash
import pickle
import pandas as pd

app = Flask(__name__)
app._static_folder = 'templates'
app.config['SECRET_KEY'] = 'supersecret'
# get the model saved earlier
model = pickle.load(open("model.pkl", "rb"))  ##loading model





@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = -1
    if request.method == 'POST':
        pregs = int(request.form.get('pregs'))
        gluc = int(request.form.get('gluc'))
        bp = int(request.form.get('bp'))
        skin = int(request.form.get('skin'))
        insulin = float(request.form.get('insulin'))
        bmi = float(request.form.get('bmi'))
        func = float(request.form.get('func'))
        age = int(request.form.get('age'))

        row_df = [[pregs, gluc, bp, skin, insulin, bmi, func, age]] 
        prediction = model.predict(row_df)
    return render_template('index.html', prediction=prediction) 
  
if __name__ == '__main__':
    app.run(debug=True)
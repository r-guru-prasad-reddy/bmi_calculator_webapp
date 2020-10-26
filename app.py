from flask import Flask, render_template, request
import pickle

import numpy as np

app = Flask(__name__)

model = pickle.load(open("C:\\Users\\lenovo\\PycharmProjects\\flaskProject\\bmi", "rb"))

# CREATOR GURU PRASAD R --- CMR INSTITUTE OF TECHNOLOGY --- STUDENT --- OPEN_TO_WORK 
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    try:
        #print(request.form)
        age = request.form['a']
        height = request.form['h']
        weight = request.form['w']
        gender = request.form['g']
        int_features = [int(height), int(weight)]
        #int_features=[int(x) for x in request.data()]
        #val = int_features[-1]
    
        if int(age)>18:
            if gender=='F' or 'f':
                int_features.append(int(0))
                int_features.append(int(1))
            elif gender =='M' or 'm':
                int_features.append(int(1))
                int_features.append(int(0))
        
            final = [np.array(int_features)]
    
    #print(int_features)
    #print(final)
            prediction = model.predict(final)

            if prediction == int(1):
                return render_template('index.html', pred="You are extremely weak, have an healthy diet")
            elif prediction == int(2):
                return render_template('index.html', pred="You are normal, Enjoy!! but you maintain it")
            elif prediction == int(3):
                return render_template('index.html', pred="You are overweight")
            elif prediction == int(4):
                return render_template('index.html', pred="Obesity!")
            elif prediction == int(5):
                return render_template('index.html', pred="Extreme obesity!")
            else:
                return render_template('index.html', pred="wrong data, please retry!")

        else:
            return render_template('index.html', pred="You are too young! Dont worry much, have an healthy food and exercise")
    except:
            return render_template('index.html', pred="Please ensure that Age, Height, Weight are numbers and Gender is either M/F")
if __name__ == '__main__':
    app.run()

# Importing the important Libraries
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) #initalizing the flask app

@app.route('/',methods=['GET']) #route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) #route to show all the predictions in web UI
@cross_origin()
def index():
    #reading the input given by Users
    Pregnancies = float(request.form['Pregnancies'])
    Glucose = float(request.form['Glucose'])
    BloodPressure = float(request.form['BloodPressure'])
    SkinThickness = float(request.form['SkinThickness'])
    Insulin = float(request.form['Insulin'])
    BMI = float(request.form['BMI'])
    DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
    Age = float(request.form['Age'])

    filename = 'modelForPredicition.sav'
    loaded_model = pickle.load(open(filename,'rb')) #loading the model file from storage
    #prediction using loaded model file
    scaler= pickle.load(open('standardScalar.sav','rb'))
    prediction = loaded_model.predict(scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]))
    print('prediction is ',prediction)
    if (prediction == 1):
        output = "Sorry! You Are A Diabetes Patient."
    else:
        output = "You Are Not A Diabetes Patient."
    print(output)
    #showing the prediction result in UI
    if (prediction == 1):
        print("Inside If")
        return render_template('results.html',output=output)
    else:
        print("Inside Else")
        return render_template('results2.html', output=output)

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
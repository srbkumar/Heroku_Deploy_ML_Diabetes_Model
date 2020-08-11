# Diabetes Prediction Model
## Heroku Link: https://ml-diabetes-pred-flask-api.herokuapp.com/
As the title suggests, this program is an end-to-end example of solving a real-world problem using Data Science. We’ll be using Machine Learning to predict whether a person has diabetes or not, based on information about the patient such as blood pressure, body mass index (BMI), age, etc.

The data was collected and made available by “National Institute of Diabetes and Digestive and Kidney Diseases” as part of the Pima Indians Diabetes Database. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here belong to the Pima Indian heritage (subgroup of Native Americans), and are females of ages 21 and above.

We’ll be using Python and some of its popular data science related packages. First of all, we will import **pandas** to read our data from a CSV file and manipulate it for further use. We will also use **numpy** to convert out data into a format suitable to feed our classification model. We’ll use **seaborn** and **matplotlib** for visualizations. We will then import Logistic Regression algorithm from **sklearn**. This algorithm will help us build our classification model. Lastly, we will use **pickle** to save our model for future use.

The following features have been provided to help us predict whether a person is diabetic or not:

**Pregnancies:** Number of times pregnant

**Glucose:** Plasma glucose concentration over 2 hours in an oral glucose tolerance test

**BloodPressure:** Diastolic blood pressure (mm Hg)

**SkinThickness:** Triceps skin fold thickness (mm)

**Insulin:** 2-Hour serum insulin (mu U/ml)

**BMI:** Body mass index (weight in kg/(height in m)2)

**DiabetesPedigreeFunction:** Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)

**Age:** Age (years)

**Outcome:** Class variable (0 if non-diabetic, 1 if diabetic)

After training of our model, we have made a flask web based API for prediction of a diabetese patient.

After that we have deployed on "Heroku" cloud platform for which link has been mentioned above.

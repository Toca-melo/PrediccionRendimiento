from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo
with open('adaboost_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            studyTimeWeekly = float(request.form['StudyTimeWeekly'])
            absences = int(request.form['Absences'])
            tutoring = int(request.form['Tutoring'])
            parentalSupport = int(request.form['ParentalSupport'])
            extracurricular = int(request.form['Extracurricular'])


            features = np.array([[studyTimeWeekly, absences, tutoring, parentalSupport, extracurricular]])
            prediction = model.predict(features)[0]

        except Exception as e:
            prediction = f'Error: {str(e)}'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

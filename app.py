import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

model =pickle.load(open('student.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=="POST":
        gender=request.form['Gender']
        ParentalSupport=request.form['ParentalSupport']
        ParentalEducation=request.form['ParentalEducation']
        StudyTimeWeekly=request.form['StudyTimeWeekly']
        Tutoring=request.form['Tutoring']
        Sports=request.form['Sports']
        Music=request.form['Music']
        Volunteering=request.form['Volunteering']
        gpa = request.form['GPA']
        Absences=request.form['Absences']
        Age=request.form['Age']
        Extracurricular=request.form['Extracurricular']
        Ethnicity=request.form['Ethnicity']

        X_test = [[
           gender,
           ParentalSupport,
           ParentalEducation,
           StudyTimeWeekly,
           Tutoring,
           Sports,
           Music,
           Volunteering,
           gpa,
           Absences,
           Age,
           Extracurricular,
           Ethnicity
        ]]
    # Make prediction
    prediction = model.predict(X_test)
    output=prediction[0]

    if(output==1.0):
            return render_template('index.html',prediction_text='Grade A')
    
    elif(output==2.0):
            return render_template('index.html',prediction_text='Grade B')
    
    elif(output==3.0):
            return render_template('index.html',prediction_text='Grade C')
    
    else:
            return render_template('index.html',prediction_text='Grade D')


if __name__ == '__main__':
    app.run(debug=True)

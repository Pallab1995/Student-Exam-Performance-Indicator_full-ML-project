from flask import Flask, request, render_template
import numpy as np
import pandas as pd 

from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Route for a home page 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    else:
        # Read all input values from form
        gender = request.form.get('gender')
        race_ethnicity = request.form.get('race_ethnicity')
        parental_level_of_education = request.form.get('parental_level_of_education')
        lunch = request.form.get('lunch')
        test_preparation_course = request.form.get('test_preparation_course')
        writing_score = float(request.form.get('writing_score'))
        reading_score = float(request.form.get('reading_score'))

        # Prepare data object
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        # Predict using pipeline
        Predict_Pipeline = PredictPipeline()
        results = Predict_Pipeline.predict(pred_df)

        # Return values back to page (so input boxes stay filled)
        return render_template(
            'home.html',
            results=round(results[0]),
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            writing_score=int(writing_score),
            reading_score=int(reading_score)
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

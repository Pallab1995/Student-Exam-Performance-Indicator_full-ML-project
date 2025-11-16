End-to-End Machine Learning Project (Flask Deployment)

This is a complete End-to-End ML Project with training pipeline, prediction pipeline, modular code structure, and a deployed Flask web application for real-time predictions.

The project follows a production-ready architecture including:

Modular ML pipeline

Training pipeline

Prediction pipeline

Flask web app

Setup file for packaging

Requirements dependency management

🚀 Project Features

Complete ML workflow: Data → Training → Model → Prediction

Modular and readable project structure

Flask web interface for taking user inputs

Real-time prediction using saved model

Setup script for installation

Deployable on Render, AWS EC2, or Azure

📂 Project Structure
ML_Project
│
├── app.py
├── application.py
├── setup.py
├── Requirements.txt
├── README.md
│
├── src
│   ├── pipelines
│   │   ├── predict_pipeline.py
│   │   └── other_pipeline_files.py
│   ├── components
│   ├── utils
│   └── ...
│
├── templates
│   ├── index.html
│   └── home.html
│
├── models
│   └── model.pkl
│
└── artifacts
    ├── preprocessor.pkl
    └── model.pkl

🧠 How the Application Works
1. User fills form on home.html

Your Flask app receives:

gender

race_ethnicity

parental_level_of_education

lunch

test_preparation_course

reading_score

writing_score

2. CustomData converts form data → DataFrame

Located in:
src/pipelines/predict_pipeline.py


app

3. PredictPipeline loads model and predicts
results = Predict_Pipeline.predict(pred_df)

4. Output is shown on home.html
🛠 How to Run Project Locally
1. Create virtual environment
python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate (Linux / Mac)

2. Install dependencies
pip install -r Requirements.txt


Requirements

3. Run the Flask app
python app.py


Your app will run on:

http://127.0.0.1:5000/

🌐 Deploying the Project
Option 1: Deploy on Render (Recommended)
1. Create a new repository on GitHub

Push your full project.

2. Go to Render → Web Services → New Web Service
3. Choose your GitHub repo
4. Fill settings:
Runtime: Python 3.10+
Build Command: pip install -r Requirements.txt
Start Command: gunicorn app:app

5. Deploy
Option 2: Deploy on AWS EC2

Launch EC2 (Ubuntu)

Install Python, pip

Clone your repo

Install requirements

Run with Gunicorn + Nginx

📌 Important Notes

For deployment, remove debug=True from Flask
(Already done in application.py) 

application

Ensure your src/ folder has __init__.py in all subfolders

Render requires gunicorn (install if needed)

📦 Packaging With setup.py

You included a clean packaging file:

python setup.py install


setup

This makes your ML pipeline installable as a package.

🙋‍♂️ Author

Pallab Sharma
Data Analyst • Machine Learning Developer
(pallabsharma100@gmail.com
)

If you want, I can also generate:

✅ README for GitHub badges (stars, forks, Python version)
✅ README banner image
✅ A downloadable .txt version of this README
Just tell me!

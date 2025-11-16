# ML_Project – Flask Application (Render Deployment)

This project is a Flask web application deployed on Render using GitHub integration. The repository name is **ML_Project**, and it contains a working Flask backend that can run both locally and in cloud hosting.

## Live Demo
Render live URL: https://student-exam-performance-indicator-9e0t.onrender.com

## Local Development (Run on Your PC)
Follow these steps to run this Flask app locally:

1. Clone the repository:
   git clone https://github.com/Pallab1995/ML_Project.git
   cd ML_Project

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Open the app in your browser:
   http://127.0.0.1:5000/

## Tech Stack
Python 3.10  
Flask  
Gunicorn  
Render Cloud Hosting  
GitHub CI Deployments  

## Project Structure
ML_Project/
app.py (main Flask application)
requirements.txt
runtime.txt
README.md
templates/ (optional)

## Deployment Instructions (Render)
1. Push your code to GitHub:
   git add .
   git commit -m "initial commit"
   git push

2. Create a file named runtime.txt:
   python-3.10.12

3. Ensure your requirements.txt includes:
   flask
   gunicorn

4. Go to Render → New → Web Service → Select GitHub → Choose ML_Project repo.

5. Use this Build Command (single line):
   pip install --upgrade pip ; pip install --no-cache-dir -r requirements.txt

6. Start Command:
   gunicorn app:app
   (If your file name is different, adjust accordingly: gunicorn main:app etc.)

7. Deploy:
   Click “Clear build cache & deploy”.

## Environment Variables
If your app requires variables, add them inside:
Render → Settings → Environment Variables

## Troubleshooting
If you see:
“gunicorn: command not found”
→ Add gunicorn to requirements.txt

If deployment fails:
→ Ensure Python version is set using runtime.txt

If app does not open on PC:
→ Make sure you visit:
   http://127.0.0.1:5000/

Check errors in:
Render → Logs → Live Tail

## Conclusion
This repository (ML_Project) contains a fully working Flask application that runs locally on http://127.0.0.1:5000/ and is deployed on Render with proper production settings(URL https://student-exam-performance-indicator-9e0t.onrender.com).

## Author
Pallab Sharma

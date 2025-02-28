# from flask import Flask, request, render_template
# import joblib
# import requests

# app = Flask(__name__)

# # Load the saved fake news classifier model
# model = joblib.load("fake_news_classifier_pipeline.pkl")

# # Hugging Face API Details
# HF_API_KEY = "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"  # Replace with your Hugging Face API key
# MODEL = "mistralai/Mistral-7B-Instruct-v0.3"  # Choose a Generative AI model

# def get_ai_explanation(article):
#     """Send a request to Hugging Face API to get an explanation of the article's credibility."""
#     url = f"https://api-inference.huggingface.co/models/{MODEL}"
#     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
#     data = {
#         "inputs": f"Analyze this news article and explain why it is fake give me answe in 100 words:\n\n{article}"
#     }

#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return "Error: Unable to generate explanation."

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     article = request.form.get('article')

#     if not article:
#         return render_template('index.html', prediction="Please enter an article!", prediction_class="neutral")

#     # Predict using the trained fake news model
#     prediction = model.predict([article])

#     if prediction[0] == 0:
#         prediction_text = "Real News"
#         prediction_class = "real"
#     else:
#         prediction_text = "Fake News"
#         prediction_class = "fake"

#     # Get AI-generated explanation
#     ai_explanation = get_ai_explanation(article)

#     return render_template(
#         'index.html', 
#         prediction=f"The article is: {prediction_text}",
#         prediction_class=prediction_class,
#         ai_explanation=ai_explanation
#     )

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, request, render_template, redirect, url_for, session
# import joblib
# import requests

# app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Change this to a secure key

# # Load the saved fake news classifier model
# model = joblib.load("fake_news_classifier_pipeline.pkl")

# # Hugging Face API Details
# HF_API_KEY = "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"  # Replace with your Hugging Face API key
# MODEL = "mistralai/Mistral-7B-Instruct-v0.3"  # Choose a Generative AI model

# def get_ai_explanation(article):
#     """Send a request to Hugging Face API to get an explanation of the article's credibility."""
#     url = f"https://api-inference.huggingface.co/models/{MODEL}"
#     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
#     data = {
#         "inputs": f"Analyze this news article and explain why it is fake. Answer in 100 words:\n\n{article}"
#     }

#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return "Error: Unable to generate explanation."

# # Login Page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Simple authentication (Replace with database authentication)
#         if username == 'admin' and password == 'password':  
#             session['user'] = username
#             return redirect(url_for('home'))
#         else:
#             return render_template('login.html', error="Invalid credentials")
    
#     return render_template('login.html')

# # Logout Route
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('login'))

# # Home Page (Fake News Detection) - Requires Login
# @app.route('/')
# def home():
#     if 'user' not in session:
#         return redirect(url_for('login'))
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     article = request.form.get('article')

#     if not article:
#         return render_template('index.html', prediction="Please enter an article!", prediction_class="neutral")

#     # Predict using the trained fake news model
#     prediction = model.predict([article])

#     if prediction[0] == 0:
#         prediction_text = "Real News"
#         prediction_class = "real"
#     else:
#         prediction_text = "Fake News"
#         prediction_class = "fake"

#     # Get AI-generated explanation
#     ai_explanation = get_ai_explanation(article)

#     return render_template(
#         'index.html', 
#         prediction=f"The article is: {prediction_text}",
#         prediction_class=prediction_class,
#         ai_explanation=ai_explanation
#     )

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, render_template, redirect, url_for, session, flash
# import joblib
# import requests
# import sqlite3  # Database to store users
# import os

# app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Change this to a secure key

# # Create database if not exists
# DB_FILE = "users.db"

# if not os.path.exists(DB_FILE):
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
#     conn.commit()
#     conn.close()

# # Load the saved fake news classifier model
# model = joblib.load("fake_news_classifier_pipeline.pkl")

# # Hugging Face API Details
# HF_API_KEY = "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"  # Replace with your Hugging Face API key
# MODEL = "mistralai/Mistral-7B-Instruct-v0.3"  # Choose a Generative AI model

# def get_ai_explanation(article):
#     """Send a request to Hugging Face API to get an explanation of the article's credibility."""
#     url = f"https://api-inference.huggingface.co/models/{MODEL}"
#     headers = {"Authorization": f"Bearer {HF_API_KEY}"}
#     data = {
#         "inputs": f"Analyze this news article and explain why it is fake. Answer in 100 words:\n\n{article}"
#     }

#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return "Error: Unable to generate explanation."

# # User Registration (Sign Up)
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         conn = sqlite3.connect(DB_FILE)
#         c = conn.cursor()
        
#         try:
#             c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#             conn.commit()
#             flash("Account created! You can now log in.", "success")
#             return redirect(url_for('login'))
#         except sqlite3.IntegrityError:
#             flash("Username already exists. Choose a different one.", "danger")

#         conn.close()
    
#     return render_template('register.html')

# # Login Page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         conn = sqlite3.connect(DB_FILE)
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session['user'] = username
#             return redirect(url_for('home'))
#         else:
#             flash("Invalid credentials. Try again.", "danger")
    
#     return render_template('login.html')

# # Logout Route
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     return redirect(url_for('login'))

# # Home Page (Fake News Detection) - Requires Login
# @app.route('/')
# def home():
#     if 'user' not in session:
#         return redirect(url_for('login'))
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'user' not in session:
#         return redirect(url_for('login'))

#     article = request.form.get('article')

#     if not article:
#         return render_template('index.html', prediction="Please enter an article!", prediction_class="neutral")

#     # Predict using the trained fake news model
#     prediction = model.predict([article])

#     if prediction[0] == 0:
#         prediction_text = "Real News"
#         prediction_class = "real"
#     else:
#         prediction_text = "Fake News"
#         prediction_class = "fake"

#     # Get AI-generated explanation
#     ai_explanation = get_ai_explanation(article)

#     return render_template(
#         'index.html', 
#         prediction=f"The article is: {prediction_text}",
#         prediction_class=prediction_class,
#         ai_explanation=ai_explanation
#     )

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for, session, flash
import joblib
import requests
import sqlite3  # Database to store users
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure key

# Create database if not exists
DB_FILE = "users.db"

if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

# Load the saved fake news classifier model
model = joblib.load("fake_news_classifier_pipeline.pkl")

# Hugging Face API Details
HF_API_KEY = "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"  # Replace with your Hugging Face API key
MODEL = "mistralai/Mistral-7B-Instruct-v0.3"  # Choose a Generative AI model

def get_ai_explanation(article):
    """Send a request to Hugging Face API to get an explanation of the article's credibility."""
    url = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    data = {
        "inputs": f"Analyze this news article and explain why it is fake. Answer in 100 words:\n\n{article}"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return "Error: Unable to generate explanation."

# User Registration (Sign Up)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Account created! You can now log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Choose a different one.", "danger")

        conn.close()
    
    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Try again.", "danger")
    
    return render_template('login.html')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Home Page (Fake News Detection) - Requires Login
@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    article = request.form.get('article')

    if not article:
        return render_template('index.html', prediction="Please enter an article!", prediction_class="neutral")

    # Predict using the trained fake news model
    prediction = model.predict([article])

    if prediction[0] == 0:
        prediction_text = "Real News"
        prediction_class = "real"
    else:
        prediction_text = "Fake News"
        prediction_class = "fake"

    # Get AI-generated explanation
    ai_explanation = get_ai_explanation(article)

    return render_template(
        'index.html', 
        prediction=f"The article is: {prediction_text}",
        prediction_class=prediction_class,
        ai_explanation=ai_explanation
    )

if __name__ == '__main__':
    app.run(debug=True)

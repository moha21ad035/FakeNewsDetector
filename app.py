from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the saved model pipeline
model = joblib.load("fake_news_classifier_pipeline.pkl")

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    article = request.form.get('article')  # Get the article from the form
    if not article:
        return render_template('index.html', prediction="Please enter an article!")

    # Predict using the model
    prediction = model.predict([article])
    prediction_text = "Real News" if prediction[0] == 0 else "Fake News"
    
    return render_template('index.html', prediction=f"The article is: {prediction_text}")

if __name__ == '__main__':
    app.run(debug=True)

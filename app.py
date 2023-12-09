from flask import Flask, request, render_template, jsonify
import joblib
import string
from flask import send_file
import os


app = Flask(__name__)

# Load the trained model
model = joblib.load('sentiment_svm_model.pkl')


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = preprocess_text(text)
        prediction = model.predict([processed_text])[0]
        sentiment = 'Positive' if prediction == 1 else 'Negative' if prediction == -1 else 'Neutral'
        return render_template('index.html', original_text=text, sentiment=sentiment)


@app.route('/download')
def downloadFile():
    # For windows you need to use drive name [ex: F:/Example.pdf]
    path = "media/sentiment-analysis-jumia-reviews.csv"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

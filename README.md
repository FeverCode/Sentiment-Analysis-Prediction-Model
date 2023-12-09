# Sentiment Analysis Flask Application

## Introduction
This Flask application performs sentiment analysis on user-provided text. It uses a trained machine learning model to classify the sentiment as positive, negative, or neutral.

[Live link to the project](https://sentiment-analysis-z1pj.onrender.com)
## Features
- Sentiment analysis of user-entered text.
- Downloadable sample dataset for testing.
- Clean and simple user interface with Bootstrap.

## Prerequisites
- Python 3
- Flask
- Other dependencies listed in `requirements.txt`

## Installation and Setup
1. Clone the repository:
```bash
git@github.com:FeverCode/Sentiment-Analysis-Prediction-Model.git
```
2. Navigate to the project directory:
```bash
cd Sentiment-Analysis-Prediction-Model
```
3. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application
1. Run the Flask application:
```bash
python app.py
```
2. Open your web browser and go to `http://127.0.0.1:5000/`.

## How to Use
- Enter the text you want to analyze in the provided text area.
- Click on 'Analyze Sentiment' to get the sentiment analysis result.
- You can also download the sample dataset to see the format of data that the model was trained on.

## Contributing
Contributions to this project are welcome. Please create a pull request or an issue in the GitHub repository.

## License
[MIT License](LICENSE)



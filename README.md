Fake-News-Detector  
Verify what you read. Trust what you know.

Fake News Detector

A machine learning-based web application that detects whether a news article is real or fake based on its content.

Table of Contents

#introduction #features #requirements #installation #usage #contributing

Introduction

The Fake News Detector is a Natural Language Processing (NLP) powered system designed to identify and flag fake news. Users can input a news article, and the model will classify it as either "real" or "fake" with a confidence score. The goal is to combat misinformation with machine learning technology.

Features

- Real-time fake news detection  
- NLP-based text preprocessing  
- TF-IDF vectorization for news content  
- Machine Learning classification using Passive Aggressive Classifier  
- Professional and animated web interface  
- API endpoint for easy integration

Requirements

- Python  
- Scikit-learn  
- Flask  
- NLTK  
- Pandas  
- HTML  
- CSS  
- JavaScript  

Installation

Clone the repository:  
git clone https://github.com/Myhfuz88Sk/fake-news-detector.git

Install dependencies:  
pip install flask pandas scikit-learn nltk joblib

Download NLTK resources:  
- punkt  
- stopwords

Usage

Train the model:
python train_model.py

Run the application:
python app.py

Access the app in your browser:
http://127.0.0.1:5000

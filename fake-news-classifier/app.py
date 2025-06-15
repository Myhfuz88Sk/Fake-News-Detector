from flask import Flask, request, jsonify, render_template
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import string

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load model and vectorizer
pac = joblib.load('passiveaggressive_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Preprocessing
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    tokens = nltk.word_tokenize(text)
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        article_text = data.get('article_text', '')
        preprocessed_text = preprocess_text(article_text)
        tfidf_text = tfidf_vectorizer.transform([preprocessed_text])
        prediction = pac.predict(tfidf_text)[0]
        confidence = pac.decision_function(tfidf_text)[0]
        normalized_confidence = float((confidence - pac.decision_function(tfidf_text).min()) /
                                       (pac.decision_function(tfidf_text).max() - pac.decision_function(tfidf_text).min() + 1e-6))
        return jsonify({'prediction': prediction, 'confidence': normalized_confidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

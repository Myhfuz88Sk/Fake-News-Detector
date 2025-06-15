# import pymysql
# from flask import Flask, request, render_template
# import pickle
# import datetime

# app = Flask(__name__)

# # Load model and vectorizer
# model = pickle.load(open('model.pkl', 'rb'))
# vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# # MySQL DB config
# db = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='4566',
#     database='fake_news_db'
# )

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     title = request.form['title']
#     text = request.form['text']
#     subject = request.form['subject']
#     date = request.form['date']

#     # Predict
#     vec_text = vectorizer.transform([text])
#     pred = model.predict(vec_text)[0]
#     result = 'Fake' if pred == 1 else 'Real'

#     # Insert into DB
#     try:
#         with db.cursor() as cursor:
#             sql = "INSERT INTO news (title, text, subject, date, label) VALUES (%s, %s, %s, %s, %s)"
#             cursor.execute(sql, (title, text, subject, date, int(pred)))
#             db.commit()
#     except Exception as e:
#         print("Error inserting into DB:", e)
#         db.rollback()

#     return render_template('index.html', prediction=result)

# if __name__ == '__main__':
#     app.run(debug=True)

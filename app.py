from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['Stock_Predictor_Users']
collection = db['Info']

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit_signup', methods=['POST'])
def submit_signup():

    name = request.form['name']
    email = request.form['email']
    contact = request.form['contact']
    pan = request.form['pan']

    collection.insert_one({
        'name': name,
        'email': email,
        'contact': contact,
        'pan': pan
    })
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

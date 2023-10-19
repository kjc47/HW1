# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is your Flask app. Scan the QR code to visit Flask documentation!'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Friends, welcome to Docker Zero To Hero'

@app.route('/health')
def health():
    return 'Server is up and running'

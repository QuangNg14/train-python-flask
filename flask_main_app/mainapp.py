from flask import Flask

app = Flask(__name__)

# https://project.com/about

@app.route('/')
def index():
    return "hello world"
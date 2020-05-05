# Application code here
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from helloworld.py"

app.run()

from flask import Flask
import os

app = Flask(__name__)

@app.get('/')
def hello():
    return "<h1>DevOps Project Successfull to version 3 </h1><p> YAY3 Running on GKE Autopilot.</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
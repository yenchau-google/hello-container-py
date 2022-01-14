from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLLLOOOOOOOOOOOOOO- this is just not really saying much"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)

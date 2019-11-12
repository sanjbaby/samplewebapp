from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test from GIT Good morning! This message is from sanju why not shown. Finallly I think I have done it"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

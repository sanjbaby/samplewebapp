from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hahahah ana mndtharam hello world! This message is from sanju why not shown. Finallly I think I have done it"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

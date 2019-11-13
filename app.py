from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('home.html')
    curl -X POST -u "apikey:FIXTaEnWS9sySkJr91J8tiNXST1ZYpu-8U4a5QJfmU_K" --header "Content-Type: audio/flac" --data - binary @ C:\Data\Container_Crush\learning\audio - file.flac "https://gateway-lon.watsonplatform.net/speech-to-text/api/v1/recognize"
if __name__ == "__main__":
    app.run(host="0.0.0.0")

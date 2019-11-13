from flask import Flask,render_template
import requests
app = Flask(__name__)

@app.route("/")

def home():

    headers = {
        'Content-Type': 'audio/flac',
    }

    data = open('C:\Data\Container_Crush\learning\audio-file.flac', 'rb').read()
    response = requests.post('https://gateway-lon.watsonplatform.net/speech-to-text/api/v1/recognize', headers=headers,
                             data=data, auth=('apikey', 'FIXTaEnWS9sySkJr91J8tiNXST1ZYpu-8U4a5QJfmU_K'))
    return render_template('home.html',value=response)
if __name__ == "__main__":
    app.run(host="0.0.0.0")

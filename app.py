
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def home():
    url = 'https://gateway-lon.watsonplatform.net/speech-to-text/api/v1/recognize'
    #headers = {'Content-Type': 'audio/flac'}
    #data = open('C:\\Data\\Container_Crush\\learning\\audio-file.flac', 'rb').read()
    #response = requests.post('https://api.us-south.speech-to-text.test.watson.cloud.ibm.com/instances/b20b578f-60a7-4e72-a3b6-08f691ff9b3b/v1/recognize', headers=headers,
     #                        data=data, auth=('apikey', 'TItad1CugTOubrsb2zXaOhswr7XB_RJvYRMn_E4hQDRO'))
    #new_value=response.json()
    #new_value=new_value['results']
    return render_template('home.html',value="Sanju")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)

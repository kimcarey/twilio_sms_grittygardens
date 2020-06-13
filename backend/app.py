from flask import Flask, request, redirect
import csv, json
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/data')
def get_state_data():
    csvFilePath = open('./data/mydata.csv', 'r')

    field_names = ("State", "County", "Grocery stores", "Supercenters & club stores", "Convenience stores",
                   "Specialized food stores", "SNAP-authorized stores", "WIC-authorized stores")

    reader = csv.DictReader(csvFilePath, field_names)
    csv.re
    out = []
    for row in reader:
       out.append(row)
    return json.dumps(out)


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    '''Respond to incoming text with simple text message'''
    resp = MessagingResponse()

    resp.message("Your Gritty Garden, coming soon.")

    return str(resp)



if __name__=='__main__':
    app.run(debug=True)
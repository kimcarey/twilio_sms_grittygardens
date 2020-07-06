from flask import Flask, request, redirect
import csv, json
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

@app.route('/', strict_slashes=False)
def index():
    return app.send_static_file('index.html')


@app.route('/data')
def get_state_data():
    csvFilePath = open('./data/mydata.csv', 'r')

    field_names = ("State", "County", "Grocery stores", "Supercenters & club stores", "Convenience stores",
                   "Specialized food stores", "SNAP-authorized stores", "WIC-authorized stores")

    reader = csv.DictReader(csvFilePath, field_names)
    out = []
    for row in reader:
       out.append(row)
    return json.dumps(out)


@app.route("/sms", methods=["GET", "POST"])
def sms_reply():
    '''Respond to incoming text with simple text message'''
    resp = MessagingResponse()

    body = request.form.get('Body')
    if body and body.isnumeric() and len(body) == 5:
        details = get_representative(body)
        if details:
            resp.message("Bring a Gritty Garden to your community. Contact your local rep: ")
            resp.message(details)
        else:
            resp.message("We don't have any details for your zip code at this time.")
    else:
        resp.message("Please provide a valid zip code.")

    return str(resp)


def get_representative(zip_code):
    import os
    myKey = os.environ.get('myKey')
    if myKey is None:
        print("Throw error?")
    # API Endpoint
    url = 'https://www.googleapis.com/civicinfo/v2/representatives'
    params = {
                'key': myKey,
                'roles': 'legislatorLowerBody',
                'address': zip_code
              }
    r = requests.get(url=url, params=params)
    data = r.json()
    print(data)
    out = ""
    # Get official's name and phone number; append to string output
    for official in data.get('officials', []):
        out += f"{official['name']} at "
        for phone in official.get('phones', []):
            out += f"{phone}"

    return out

if __name__=='__main__':
    app.run(debug=True)
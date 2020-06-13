from flask import Flask
import csv, json




app = Flask(__name__)

@app.route('/data')
def get_state_data():
    csvFilePath = open('./data/mydata.csv', 'r')
    # jsonFilePath = open('mydata.json', 'w')

    field_names = ("State", "County", "Grocery stores", "Supercenters & club stores", "Convenience stores",
                   "Specialized food stores", "SNAP-authorized stores", "WIC-authorized stores")

    reader = csv.DictReader(csvFilePath, field_names)
    out = []
    for row in reader:
        # json.dump(row, jsonFilePath)
        # jsonFilePath.write('\n')
        out.append(row)
    return json.dumps(out)

if __name__=='__main__':
    app.run(debug=True)
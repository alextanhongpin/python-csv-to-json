from flask import Flask, render_template, request

import csv
import json
from io import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>')
def index(name=None):
    csv_text = ''
    if request.method == 'POST':
        csv_text = request.form['csv_text']
        f = StringIO(csv_text)
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        output = []
        for row in reader:
            j = {}
            for i, _ in enumerate(fieldnames):
                j[fieldnames[i]] = row[fieldnames[i]]
            output.append(j)
        name = json.dumps(output)
    
    return render_template('index.html', name=name, csv_text=csv_text)


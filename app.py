import json
import os
from flask import Flask, render_template, request


app = Flask(__name__)

if os.path.exists("data.json"):
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data)
else: 
    # create a new empty file with 0 visitors
    data = {"visitors": 0}
    with open("data.json", "w") as file:
        file.write(json.dumps(data))
        
def flush():
    with open("data.json", "w") as file:
        file.write(json.dumps(data))

@app.route("/")
def add_visitor():
    data["visitors"] += 1
    flush()
    return render_template("index.html", visitors=data["visitors"])
    
@app.route("/", methods=['POST'])
def get_covid_url():
    visitors = data["visitors"]
    text = request.form["country"]
    url = f'https://covidstats-sdbd.onrender.com/?country={text}'
    print(url)
    return render_template("index.html", visitors=visitors, img=url)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)
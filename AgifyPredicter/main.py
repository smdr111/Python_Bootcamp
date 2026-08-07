from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route("/guess/<name>")
def guess(name):
    gen_response = requests.get("https://api.genderize.io", params={f"name": f"{name}"})
    gen_response.raise_for_status()
    age_response = requests.get("https://api.agify.io", params={"name": f"{name}"})
    age_response.raise_for_status()
    age = age_response.json()['age']
    gen = gen_response.json()['gender']
    return render_template("index.html",gen=gen,age=age,name=name)

if __name__ == "__main__":
    app.run(debug=True)
from crypt import methods
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():
    quantity = request.form.get("quantity")
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=5"
    response = requests.get(url)
    print(response.json())

    return render_template("search.html",quantity=quantity,response=response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
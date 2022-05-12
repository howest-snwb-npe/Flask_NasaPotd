from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/search")
def search():
    quantity = request.args.get("quantity")
    return render_template("search.html",quantity=quantity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
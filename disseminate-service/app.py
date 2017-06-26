from flask import Flask, render_template, request
import os

# ----- Routes definition
app = Flask(__name__)

finalProduct = "YO"

@app.route("/")
def home():
    return render_template("index.html", product=finalProduct)

@app.route("/product", methods = ["PUT"])
def product():
    print("Request incoming on /product")
    payload = request.data.decode("UTF-8")
    finalProduct = payload
    return "OK"

@app.route("/infos")
def infos():
    return "Some infos on disseminate-service"

app.run(debug=False, host="0.0.0.0")

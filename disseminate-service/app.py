from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

# ----- Routes definition
app = Flask(__name__)


finalProduct = "default"

@app.route("/")
def home():
    return render_template("index.html", product=finalProduct, timestamp=datetime.now())

@app.route("/product", methods = ["PUT"])
def product():
    print("Request incoming on /product")
    data = request.data.decode("UTF-8")
    global finalProduct
    finalProduct = data
    print("Final product is now " + finalProduct)
    return "OK"

@app.route("/infos")
def infos():
    return jsonify({ "product": finalProduct, "timestamp": datetime.now() })

app.run(debug=False, host="0.0.0.0")

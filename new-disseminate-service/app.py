from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

finalProduct = {
    "totalNumberOfRespondents": 0,
    "totalNumberOfChildren": 0,
    "occupations": []
}

@app.route("/")
def home():
    return render_template("index.html", product=finalProduct)

@app.route("/product", methods = ["PUT"])
def product():
    print("Request incoming on /product")
    data = request.data.decode("UTF-8")
    print("data is of type: " + str(type(data)))
    global finalProduct
    finalProduct = json.loads(data)
    print("Final product is now " + str(finalProduct))
    return "OK"

@app.route("/infos")
def infos():
    return jsonify({ "product": finalProduct, "timestamp": datetime.now() })

app.run(debug=False, host="0.0.0.0")

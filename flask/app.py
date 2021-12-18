from flask import Flask
from flask import request
from flask import jsonify
from models import get_data
import pandas as pd


app = Flask(__name__)


@app.route("/api/flask", methods=['POST', 'GET'])
def api():
    _user_id = request.args.get('uid')
    _product_id = request.args.get('prodid')
    _store_id = request.args.get('storeid')
    gt = get_data(_user_id, _product_id, _store_id)
    result = gt.df()
    if _user_id == None or _product_id == None or _store_id == None:
        final = "404 Data Not Found"
    elif len(result) <= 2:
        final = "404 Data Not Found"
    else:
        final = result
    return final

@app.route("/")
def homepage():
    return jsonify(
        username="long",
        email="test@gmail.com",
        id=566
    )
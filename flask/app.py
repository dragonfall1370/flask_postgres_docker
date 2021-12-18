from flask import Flask
from flask import request
from flask import jsonify
from models import get_data
import pandas as pd
import os

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
    return """<!DOCTYPE html>
                    <html>

                    <head>
                    <title>Our Test Page</title>
                    </head>

                    <body>

                    <h1>Welcome to Our Page</h1>
                    <h2>Web Site Main Ingredients:</h2>

                    <p>Pages (HTML)</p>
                    <p>Style Sheets (CSS)</p>
                    <p>Computer Code (JavaScript)</p>
                    <p>Live Data (Files and Databases)</p>

                    </body>
                    </html>"""

@app.route("/data")
def data():
    return jsonify(
        username="long",
        email="test@gmail.com",
        id=566
    )
if __name__=="__main__":
    app.run(debug=True, ssl_context='adhoc')
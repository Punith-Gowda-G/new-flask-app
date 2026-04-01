from flask import Flask, jsonify
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/posts")
def posts():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/posts").json())
        "data": response.json(),
        "status": "successfully triggered auto deployment",
        "status_code": 200
    
@app.route("/comments")
def comments():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/comments").json())
        "data": response.json(),
        "status": "successfully triggered auto deployment",
        "status_code": 200
    
@app.route("/albums")
def albums():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/albums").json())
        "data": response.json(),
        "status": "successfully triggered auto deployment",
        "status_code": 200


if __name__ == "__main__":
    app.run(debug=True)

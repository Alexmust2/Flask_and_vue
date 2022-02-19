from flask import Flask, json, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

users_list = [
    {"id": 0, "name": "Sasa", "city": "Moscow"},
    {"id": 1, "name": "Andrei", "city": "Moscow"},
    {"id": 2, "name": "Sergei", "city": "Moscow"},
    {"id": 3, "name": "Lilia", "city": "Moscow"}
]
post_list = [
    {"id": 0, "title": "how to learn python", "content": "dadad", "owner": 0},
    {"id": 1, "title": "how to learn html", "content": "klklk", "owner": 0},
    {"id": 2, "title": "how to learn css", "content": "cvcvcv", "owner": 1},
    {"id": 3, "title": "how to learn vuejs", "content": "vbvbvb", "owner": 2}
]

@app.route('/users')
def users():
    return jsonify(users_list)

@app.route('/post')
def post():
    return jsonify(post_list)

if __name__ == '__main__':
    app.run(debug=True)
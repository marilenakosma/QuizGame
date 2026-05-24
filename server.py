from flask import Flask,jsonify,request
from db import get_scores,save_score

app = Flask(__name__)

@app.route('/scores/<username>', methods=['GET'])
def fetch_scores(username):
    return jsonify(get_scores(username))

if __name__== '__main__':
    app.run(port=5000)
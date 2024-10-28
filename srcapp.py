# src/app.py
from flask import Flask, jsonify
from model import get_recommendations

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def recommendations():
    return jsonify({"recommendations": get_recommendations()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
from src.classifier import classify

app = Flask(__name__)
CORS(app)

@app.route('/classify', methods=['POST'])
def classify_route():
    data = request.get_json(force=True)
    text = data.get('text', '')
    result = classify(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
import magic, io
from pypdf import PdfReader
from src.classifier import classify
from src.utils import extract_text


app = Flask(__name__)
CORS(app)

@app.route("/extract-text", methods=["POST"])
def extract_route():
    """
    Recebe form-data com 'file' e devolve {'text': ...}
    """
    if "file" not in request.files:
        return jsonify({"error": "Arquivo não enviado"}), 400

    try:
        text = extract_text(request.files["file"])
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"text": text})

@app.route("/classify", methods=["POST"])
def classify_route():
    if not request.is_json:
        return jsonify({"error": "Envie JSON com 'text'"}), 400

    text = request.get_json(force=True).get("text", "")
    return jsonify(classify(text))


if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
from flask_cors import CORS
import magic, io
from pypdf import PdfReader
import joblib
from src.classifier import classify_zeroshot, classify_logreg
from src.utils import extract_text


app = Flask(__name__)
CORS(app)

clf = joblib.load("src/models/modelo_produtivo.joblib")
vectorizer = joblib.load("src/models/vectorizer.joblib")

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

    data = request.get_json(force=True)
    text = data.get("text", "")
    model = data.get("model", "zeroshot")

    if model == "reglog":
        print("Classificando com Regressão Logística...")
        result = classify_logreg(text)
    else:
        print("Classificando com Zero-Shot...")
        result = classify_zeroshot(text)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

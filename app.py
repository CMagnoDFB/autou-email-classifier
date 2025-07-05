from flask import Flask, request, jsonify
from flask_cors import CORS
import magic, io
from pypdf import PdfReader
from src.classifier import classify
app = Flask(__name__)
CORS(app)

def extract_text(file_storage):
    buf = file_storage.read()
    mime = magic.from_buffer(buf, mime=True)

    if mime == "text/plain":
        return buf.decode("utf-8", errors="ignore")

    if mime == "application/pdf":
        reader = PdfReader(io.BytesIO(buf))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    raise ValueError("Formato não suportado")

@app.route("/classify", methods=["POST"])
def classify_route():
    # 1) Se veio JSON com 'text', fluxo mais direto
    if request.is_json:
        text = request.get_json(force=True).get("text", "")
        out = classify(text)
        return jsonify(out)

    # 2) Form-data com arquivo
    if "file" in request.files:
        try:
            text = extract_text(request.files["file"])
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        out = classify(text)
        return jsonify(out)

    return jsonify({"error": "Nenhum texto ou arquivo enviado."}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)

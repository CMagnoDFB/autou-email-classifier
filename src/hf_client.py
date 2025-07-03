import os, requests, json
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN", "")

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
)

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}

def hf_zero_shot(text: str, labels=("Email produtivo em relação ao trabalho", "Email improdutivo em relação ao trabalho")) -> dict:
    """
    Classifica o texto usando o inferência de modelo zero-shot da Hugging Face.
    Retorna um dicionário com a categoria e a pontuação.
    """
    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": list(labels)},
        "options": {"wait_for_model": True}
    }

    resp = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    best = max(zip(data["labels"], data["scores"]), key=lambda t: t[1])
    return {"label": best[0], "score": best[1]}
from src.hf_client import hf_zero_shot
from src.hf_gen import generate_reply


def classify(email_text: str) -> dict:
    """
    Recebe texto cru de email.
    Retorna dicionário com categoria e resposta placeholder.
    """

    result = hf_zero_shot(email_text)
    categoria = result["label"]
    confianca = round(result["score"], 2)

    resposta = generate_reply(email_text, categoria)

    return {
        "categoria": categoria,
        "score": confianca,
        "resposta": resposta
    }
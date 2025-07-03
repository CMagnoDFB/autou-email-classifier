from src.hf_client import hf_zero_shot


def classify(email_text: str) -> dict:
    """
    Recebe texto cru de email.
    Retorna dicionário com categoria e resposta placeholder.
    """

    result = hf_zero_shot(email_text)
    categoria = result["label"]

    resposta = "RESPOSTA TODO"  # Placeholder para resposta gerada por LLM

    return {
        "categoria": categoria,
        "score": round(result["score"], 2),
        "resposta": resposta # será gerada por uma LLM
    }
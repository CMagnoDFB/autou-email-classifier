from src.hf_client import hf_zero_shot
from src.hf_gen import generate_reply


def classify_zeroshot(email_text: str) -> dict:
    """
    Recebe texto cru de email.
    Retorna dicionário com categoria e resposta placeholder.
    """

    result = hf_zero_shot(email_text)
    categoria = result["label"]
    if categoria == "requer uma ação de trabalho ou resposta específica de trabalho.":
        categoria = "Produtivo"
    elif categoria == "não requer uma ação imediata de trabalho ou resposta específica de trabalho.":
        categoria = "Improdutivo"
    
    
    confianca = round(result["score"], 2)

    resposta = generate_reply(email_text, categoria)

    return {
        "categoria": categoria,
        "score": confianca,
        "resposta": resposta
    }

def classify_logreg(email_text: str) -> dict:
    """
    Classifica com modelo clássico treinado.
    """
    from app import clf, vectorizer  # pega os já carregados

    from src.preprocessing import preprocess  # sua função de limpeza do texto

    email_clean = preprocess(email_text)
    X_vec = vectorizer.transform([email_clean])
    pred = clf.predict(X_vec)[0]
    probas = clf.predict_proba(X_vec)[0]

    categoria = "Produtivo" if pred == 1 else "Improdutivo"
    confianca = round(max(probas), 2)

    resposta = generate_reply(email_text, categoria)

    return {
        "categoria": categoria,
        "score": confianca,
        "resposta": resposta
    }
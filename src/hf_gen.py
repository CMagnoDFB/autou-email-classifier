import os, requests, json, textwrap, time
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()

CLIENT_GEN = InferenceClient(
    model   = os.getenv("HF_LLM_MODEL"),
    token   = os.getenv("HF_API_TOKEN"),
    provider="novita",
    timeout = 90
)

def generate_reply(email_text: str, category: str) -> str:
    """
    Gera uma resposta para o email usando um modelo LLM da Hugging Face.
    
    Args:
        email_text (str): Texto do email a ser respondido.
        category (str): Categoria do email (ex: "Produtivo", "Improdutivo").

    Returns:
        str: Resposta gerada pelo modelo LLM.
    """

    if (category == "requer uma ação de trabalho ou resposta específica de trabalho." or category == "Produtivo"):
        

        system_pt = (
        "Você é um assistente de uma grande empresa do setor financeiro. Sua tarefa é sugerir uma resposta automática adequada à categoria identificada."

        "**Instruções:**"
        "1.  Analise o conteúdo do e-mail do cliente para identificar a **intenção principal** (ex: solicitação de status, dúvida sobre o sistema, problema técnico, etc.)."
        "2.  Elabore uma resposta que seja direta, profissional e ajude a resolver a questão do cliente ou forneça a informação solicitada."
        "3.  **Utilize placeholders** para informações dinâmicas que precisariam ser preenchidas posteriormente pela equipe. Os placeholders devem estar entre colchetes, por exemplo: '[Nome do Cliente]', '[ID da Solicitação]', '[Data Prevista]', '[Departamento Responsável]'."
        "4.  Mantenha um tom cortês e prestativo."
        "5.  A resposta deve ser preparada para ser um rascunho a ser revisado e finalizado por um operador humano."
        "6.  Responda sempre em português brasileiro."
        "7. Sua resposta deve ter no máximo 120 palavras."

        "**Formato da Saída:**"
        "Gere apenas o texto da resposta. Não inclua saudações adicionais como 'Atenciosamente' ou assinaturas."     
        )
    
    elif (category == "não requer uma ação imediata de trabalho ou resposta específica de trabalho." or category == "Improdutivo"):
        

        system_pt = (
        "Você é um assistente de suporte ao cliente de uma grande empresa do setor financeiro. Sua tarefa é sugerir uma resposta automática adequada à categoria identificada."

        "**Instruções:**"
        "1.  A resposta deve ser breve e amigável."
        "2.  Não inclua nenhum placeholder ou informação específica do e-mail."
        "3.  A resposta deve ser um agradecimento genérico ou uma mensagem de reconhecimento."
        "4.  Responda sempre em português brasileiro."

        "**Formato da Saída:**"
        "Gere apenas o texto da resposta. Não inclua saudações adicionais como 'Atenciosamente' ou assinaturas."
        )

    print(f"Gerando resposta para categoria: {category}")
    
    user_prompt = textwrap.dedent(f"""
        Categoria do e-mail: {category}.
        Email recebido:
        ```
        {email_text.strip()}
        ```        
    """).strip()

    messages = [
        {"role": "system", "content": system_pt},
        {"role": "user", "content": user_prompt}
    ]

    out = CLIENT_GEN.chat_completion(
        messages=messages,
        max_tokens=256,
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.0,
        frequency_penalty=0.0,
    )
    
    return out.choices[0].message.content.strip()

    
    
        
        
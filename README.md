# 📧 AutoU - Email Classifier

MVP para o processo seletivo AutoU 🚀

Este projeto classifica e-mails como produtivos ou improdutivos, e sugere automaticamente uma resposta adequada ao conteúdo.

## ✨ Funcionalidades

Classificação automática de e-mails em duas categorias:

Produtivo: requer ação ou resposta

Improdutivo: mensagens sociais, sem demanda

Sugestão de resposta automática com base na categoria e no conteúdo

Opção de dois métodos de classificação:

Zero-Shot (mDeBERTa-v3-base-mnli-xnli via HuggingFace Inference API)

Regressão Logística (modelo treinado localmente sobre dataset sintético)

## 🖥️ Tecnologias utilizadas

### Backend

Flask — API web

Gunicorn — WSGI server para produção

spaCy — pré-processamento de texto e lematização

scikit-learn — regressão logística

HuggingFace Hub — modelos mDeBERTa e Mistral para inferência

pypdf e python-magic — extração de texto de arquivos

### Frontend

React + Vite

Seleção dinâmica do método de classificação

Upload de arquivos ou entrada manual de texto

Treinamento do modelo
Notebook Jupyter Lab para criação e salvamento do modelo de Regressão Logística

## 📂 Estrutura do projeto

```
.
├── app.py                    # Backend Flask
├── src/                      # Código backend
│   ├── classifier.py
│   ├── hf_client.py
│   ├── hf_gen.py
│   ├── preprocessing.py
│   └── utils.py
├── frontend/                 # Frontend Vite/React
├── notebooks/                # Notebooks para experimentos e treinamento
│   ├── treino.ipynb
│   └── emails_sinteticos.csv
├── samples/                  # Exemplos de e-mails
├── requirements.txt          # Dependências mínimas para produção
├── requirements-dev.txt      # Dependências completas para desenvolvimento
└── README.md
```

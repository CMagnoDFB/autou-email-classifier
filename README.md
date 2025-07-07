# 📧 AutoU - Email Classifier

Case prático para o processo seletivo AutoU 🚀

Este projeto é uma aplicação web que classifica e-mails como produtivos ou improdutivos, e sugere automaticamente uma resposta adequada ao conteúdo.

## 🌐 Links públicos

| Recurso | URL |
|---------|-----|
| **App Web** (frontend React, Vercel) | https://autou-email-classifier.vercel.app |
| **API** (backend Flask, Render) | https://autou-email-classifier-xvbn.onrender.com |
| **Vídeo-demo (YouTube, 4 min)** | https://youtu.be/NEpcGYV5G_A |
| **Repositório GitHub** | https://github.com/CMagnoDFB/autou-email-classifier |

## ⚠️ Limitações dos planos gratuitos

| Plataforma         | Limitação principal |
|--------------------|---------------------|
| **Render (Free)**  | Serviços web entram em hibernação após ~15 min sem uso. Ao receber uma nova requisição, pode levar **30–60 s** para “acordar” o servidor ([render.com](https://render.com/docs/free)). |
| **Vercel (Hobby)** | Frontend estático é rápido, mas se tivessem sido usadas funções serverless (não usadas aqui), há cold-starts de **1–2 s**, e funções têm limite máximo de **10 s** de execução. |

> 💡 **Nota:** em uso contínuo, a aplicação responde rapidamente, mas esteja preparado para uma **latência inicial**, especialmente se estiver inativa há algum tempo.

## ✨ Funcionalidades

#### Classificação automática de e-mails em duas categorias:

- Produtivo: requer ação ou resposta

- Improdutivo: mensagens sociais, sem demanda

Sugestão de resposta automática com base na categoria e no conteúdo.

#### Opção de dois métodos de classificação:

- Zero-Shot (mDeBERTa-v3-base-mnli-xnli via HuggingFace Inference API)

- Regressão Logística (modelo treinado localmente sobre dataset sintético)

## 🖥️ Tecnologias utilizadas

### Backend

- Flask — API web

- Gunicorn — WSGI server para produção

- spaCy — pré-processamento de texto e lematização

- scikit-learn — regressão logística

- HuggingFace Hub — modelos mDeBERTa e Mistral para inferência

- pypdf e python-magic — extração de texto de arquivos

### Frontend

- React + Vite

- Seleção dinâmica do método de classificação

- Upload de arquivos ou entrada manual de texto

### Treinamento do modelo
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


### 🧑‍💻 Rodando localmente

Você também pode rodar a aplicação localmente para desenvolvimento ou testes:

#### 🔷 Pré-requisitos

- Python 3.10+ com virtualenv
- Node.js 18+ com npm

##### 🔷 Backend

```bash
# Na raiz do projeto
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

pip install -r requirements-dev.txt
python app.py
O backend estará disponível em: http://localhost:5000
```
##### 🔷 Frontend

```bash

cd frontend
npm install
npm run dev
```
O frontend estará disponível em: http://localhost:5173

Por padrão, ele já está configurado para usar o backend local (http://localhost:5000).

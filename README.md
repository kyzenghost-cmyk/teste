# Simple Flask App

Este repositório contém um aplicativo Flask minimalista que responde com uma mensagem simples na raiz.

## Estrutura
```
python_app/
├─ app.py            # Código do Flask
└─ requirements.txt # Dependências
```

## Como rodar localmente
```bash
# Clone o repositório
git clone https://github.com/kyzenghost-cmyk/teste.git
cd teste/python_app

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
python app.py
```

O aplicativo estará disponível em `http://localhost:5000`.

## Deploy
O código já usa a variável de ambiente `PORT`, o que permite deploy fácil em plataformas como Heroku, Render, Railway etc.

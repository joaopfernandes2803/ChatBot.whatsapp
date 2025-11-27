# ChatBot.whatsapp

Um chatbot desenvolvido em Python usando FastAPI, projetado para receber e responder mensagens via webhook (ideal para WhatsApp, APIs externas e automações). O projeto serve como base simples e organizada para criar bots e integrações com serviços externos.

## Tecnologias usadas
- Python 3.x  
- FastAPI  
- Uvicorn  
- Requests  
- python-dotenv  

## 📁 Estrutura do projeto
ChatBot.whatsapp/
│
├── src/
│ ├── webhook.py – recebe mensagens via webhook
│ └── message_handler.py – lógica de processamento das mensagens
│
├── main.py – inicializa a aplicação FastAPI
├── configuracao.py – configurações e variáveis de ambiente
├── requeriments.txt – dependências
└── README.md

##  Como rodar
1. Clone o repositório  
   ```bash
   git clone https://github.com/joaopfernandes2803/ChatBot.whatsapp
   cd ChatBot.whatsapp
   
python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requeriments.txt

uvicorn main:app --reload --port 8000



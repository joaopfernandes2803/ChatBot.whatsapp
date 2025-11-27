from fastapi import FastAPI
from src.webhook import router as webhook_router

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'WhatsApp Bot is running'}

app.include_router(webhook_router)
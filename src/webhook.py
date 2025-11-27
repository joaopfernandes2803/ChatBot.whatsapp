from fastapi import APIRouter, Request
from configuracao import META_VERIFY_TOKEN
from src.message_handler import process_message

router = APIRouter()

@router.get('/webhook')
async def verify_token(mode: str, challenge: str, token: str):
    if mode == "subscribe" and token == META_VERIFY_TOKEN:
        return int(challenge)
    return {'erro': 'Token inválido'}

@router.post('/webhook')
async def receive_message(request: Request):
    body = await request.json()
    try:
        entry = body['entry'][0]['changes'][0]['value']
        messages = entry.get('messages')
        if messages:
            msg = messages[0]
            await process_message(msg)
    except:
        pass
    return {'status': 'ok'}

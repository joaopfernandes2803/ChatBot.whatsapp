from configuracao import META_ACCESS_TOKEN, PHONE_NUMBER_ID
import requests

async def send_whatsapp_message(to, text):
    url= f'https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages'

    data = {
        'messaging_product': 'whatsapp',
        'to': to,
        'text': {'body': text}
    }
    headers = {
        'Authorization': f'Bearer {META_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
async def process_message(message):
    user_number = message['from']
    text = message.get('text', {}).get('body','')

    if 'oi' in text .lower():
        await send_whatsapp_message(user_number, 'Olá! Como posso ajudar você?')
    else:
        await send_whatsapp_message(user_number,'Recebi sua mensagem!')

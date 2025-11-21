from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8281069430:AAHSopUfUvnoCEsHXH0UusYToxfnQcSkN-A"

@app.route('/')
def home():
    return "Bot is working"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        if text == '/start':
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": "Пр бро нажми на эту кнопку",
                "reply_markup": {
                    "inline_keyboard": [[{
                        "text": "Открыть",
                        "web_app": {"url": "https://ТВОЙ-САЙТ.netlify.app"}
                    }]]
                }
            }
            requests.post(url, json=payload)
    
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
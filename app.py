from flask import Flask, request
import requests

app = Flask(__name__)

# ВАШ ТОКЕН
BOT_TOKEN = "7972371687:AAGSfOYn61dl2APWJ7KtIqOx1V_UcqHkb2Q"
VIDEO_URL = "https://cdn.jsdelivr.net/gh/galaxxyy123/tg-bot-anim@main/tg-bot-anim.mp4"

@app.route('/')
def home():
    return 'Бот работает! ✅'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # Проверяем команду /start
    if 'message' in data and 'text' in data['message']:
        text = data['message']['text']
        chat_id = data['message']['chat']['id']
        
        if text == '/start':
            # Отправляем видео
            send_video(chat_id)
    
    return 'OK'

# Функция отправки видео
def send_video(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    data = {
        "chat_id": chat_id,
        "video": VIDEO_URL
    }
    requests.post(url, json=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

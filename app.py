from flask import Flask
import requests
from threading import Thread
import time

app = Flask(__name__)

# ВАШ ТОКЕН
BOT_TOKEN = "7972371687:AAGSfOYn61dl2APWJ7KtIqOx1V_UcqHkb2Q"
VIDEO_URL = "https://cdn.jsdelivr.net/gh/galaxxyy123/tg-bot-anim@main/tg-bot-anim.mp4"

@app.route('/')
def home():
    return 'Бот работает! ✅'

@app.route('/webhook', methods=['POST'])
def webhook():
    return ''

# Простая функция для отправки видео
def send_video(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    data = {
        "chat_id": chat_id,
        "video": VIDEO_URL
    }
    requests.post(url, json=data)

# Настройка вебхука
def setup_webhook():
    time.sleep(10)
    webhook_url = "https://tg-bot-anim.onrender.com/webhook"
    set_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={webhook_url}"
    requests.get(set_url)
    print("Webhook настроен!")

# Запускаем настройку вебхука
Thread(target=setup_webhook).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

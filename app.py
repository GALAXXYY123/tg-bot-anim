from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio
import requests
from threading import Thread
import time

app = Flask(__name__)

# ВАШ ТОКЕН
BOT_TOKEN = "7972371687:AAGSfOYn61dl2APWJ7KtIqOx1V_UcqHkb2Q"
# ПРАВИЛЬНАЯ ССЫЛКА С .mp4
VIDEO_URL = "https://cdn.jsdelivr.net/gh/galaxxyy123/tg-bot-anim@main/tg-bot-anim.mp4"

# Создаем бота
bot_app = Application.builder().token(BOT_TOKEN).build()

# Отправка видео
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_video(video=VIDEO_URL)

# Добавляем обработчик
bot_app.add_handler(CommandHandler("start", start))

# Вебхук для Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    asyncio.run(bot_app.process_update(update))
    return ''

@app.route('/')
def home():
    return ''

# Автоматическая настройка вебхука при запуске
def setup_webhook():
    time.sleep(5)  # Ждем запуск сервера
    webhook_url = "https://tg-bot-anim.onrender.com/webhook"
    set_webhook_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={webhook_url}"
    try:
        response = requests.get(set_webhook_url)
        print("Webhook setup result:", response.json())
    except Exception as e:
        print("Webhook setup error:", e)

# Запускаем настройку вебхука в фоновом режиме
Thread(target=setup_webhook).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

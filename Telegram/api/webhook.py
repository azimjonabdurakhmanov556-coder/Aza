from flask import Flask, request
import telebot
import os

TOKEN = os.environ.get('BOT_TOKEN', '8903255663:AAGH2-Ak0vZx0iw9Bzkr8t3RtPc0LFS84cg')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return '!', 200

@app.route('/')
def index():
    return 'Bot ishlayapti!'

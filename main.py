from pyrogram import Client, filters
import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_KEY = os.environ.get("API_KEY")

app = Client("kekereplybot", bot_token=BOT_TOKEN)

def ask_ai(text):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": text}]
    }

    r = requests.post(url, headers=headers, json=data)
    return r.json()["choices"][0]["message"]["content"]

@app.on_message(filters.text)
def reply(client, message):
    try:
        res = ask_ai(message.text)
        message.reply(res)
    except:
        message.reply("AI error 😢")

app.run()

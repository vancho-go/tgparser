from flask import Flask, request
import requests
import json
import configparser

app = Flask(__name__)

def send_message(chat_id):
  method = "sendMessage"
	# Считываем учетные данные
  config = configparser.ConfigParser()
  config.read("config.ini")

  token = config['Telegram']['bot_token_flask']
  url = f"https://api.telegram.org/bot{token}/{method}"

  with open ('channel_messages.json') as f:
    messages_json = json.load(f)

  for i in range(len(messages_json)-1):
    try:
			# print(f'number {i}')
			# print(messages_json[i]['message'])
      data = {"chat_id": chat_id, "text": messages_json[i]['message']}
      requests.post(url, data=data)
    except:
      pass



@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        send_message(chat_id)
    return {"ok": True}
import telebot
from flask import Flask, request


app = Flask(__name__)


url = "https://843c-105-112-44-166.eu.ngrok.io/"
token = "5936136679:AAGD3tx2pwtO9sPAgaj9ccKBzrESTG0zmZ8"

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing from richie?")


@app.route("/", methods=["GET"])
def index():
    return "Holla at your boy server is up"


@app.route("/" + token, methods=["POST"])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "Got the message"


@app.route("/hook")
def webhook():
    bot.remove_webhook()
    print(url + token)
    bot.set_webhook(url + token)
    return f"Webhook set to {url}"


debug = False
if debug == True:
    bot.infinity_polling()
else:
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5009)

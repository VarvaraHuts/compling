#бот присваивает либо положительную, либо отрицательную оценку отзыву (кафе/рестораны)

import telebot, flask, conf
from pymystem3 import Mystem

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(TOKEN, threaded=False)

bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)

m = Mystem()

v = open("/home/hsecompling2017/mysite/sentilexposneg.csv", "r", encoding="Windows-1251")
lines = v.readlines()
dic = {}
for line in lines:
    line = line.strip("\n")
    line = line.split(",")
    word_ton = line[0]
    ton = line[1]
    dic[word_ton] = ton

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "hi! i will appraise your review")

@bot.message_handler(func=lambda m: True)
def define_ton(message):
    text = str(message.text)
    res = m.lemmatize(text)
    res_f = "".join(res)
    res_f = res_f.strip("\n")
    res_f = " " + res_f + " "

    pos = 0
    neg = 0
    for key, value in dic.items():
        if " " + key + " " in res_f and value == " positive":
            if "не " + key not in res_f and "не" + key not in res_f:
                if '"' + key + '"' not in res_f:
                    pos += 1
            else:
                neg += 1
        if " " + key + " " in res_f and value == " negative":
            if "не " + key not in res_f and "не" + key not in res_f:
                neg += 1
            else:
                pos += 1
    if pos - neg > 0:
        score = "positive"
    else:
        score = "negative"

    bot.send_message(message.chat.id, score)

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

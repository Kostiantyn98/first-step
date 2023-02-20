import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = "https://etnosvit.com/uk/anekdoty_uk/pro-putina.html"
API_KEY = "6149714194:AAHkyYqCwjKzZhROyTKSnuX6EKmnT0H_Rz0"
def parser(url):
    r = requests.get(url)
# print(r.status_code)
    soup = b(r.text, "html.parser")
    anekdots = soup.find_all("div", class_="su-quote-inner su-u-clearfix su-u-trim")
# print(anekdots)
    return [i.text for i in anekdots]

jokes = parser(URL)
random.shuffle(jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands = ["start"])
def hello(message):
    bot.send_message(message.chat.id, "Путін ху##о!Натисну цифру: ")

@bot.message_handler(content_types=['text'])
def joke(message):
    if message.text.lower() in "123456789987654321":
        bot.send_message(message.chat.id, jokes[0])
        del jokes[0]
        return bot.send_message(message.chat.id, "Щоб отримати ще порцію гумору натисніть цифру:  ")
    else:
        pass
        # bot.send_message(message.chat.id, "Щоб отримати ще порцію гумору натисніть цифру:  ")
bot.polling()







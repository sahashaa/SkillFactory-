import telebot  #Импортируем модуль бота

from botconfig import *  #Переносим все конфиги в "Сердце" бота
from botclass import APIexception
from botclass import Converter
import traceback


bot = telebot.TeleBot(TOKEN)  #Привязка бота к токену

#Заставляем бота не остонавливать при ошибках

@bot.message_handler(commands=['start', 'help'])  #показываем боту на какие команды нудно реагировать
def hello_machine(message):  #сообщение которое будет отправлять бот в ответ на команды
    htext = f"Добрый день дорогой {message.chat.username},добро пожаловать Этот бот курса валют для обмена вам нужно ввести по форме<имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>для получения списка валют напишите /values"
    bot.reply_to(message, htext)  #Бот отвечает на сообщение вышенаписанным текстом

@bot.message_handler(commands=['values'])  #та команда на которую будет реагировать бот для "Выдачи" списка доступных валют
def open_values(message: telebot.types.Message):
    vtext = 'Доступные валюты на данный момент:'
    for i in vis_values:  #делаем цикл фор,для прохождения по списку достуипных валют
       vtext = '\n'.join((vtext, i))  #используем джоин и \n для того чтобы получился раздельный список
    bot.reply_to(message, vtext)  #бот отвечаает на наше сообщение

@bot.message_handler(content_types=['text'])  #На какой тип данных бот будет реаигироваитб
def convert(message:telebot.types.Message):

        values= message.text.split()  #сплитуем для того чтобы получился список занчений
        try:
            if len(values) != 3:
                raise APIexception('Неверное количество параметров!')

            answer = Converter.get_price(*values)
        except APIexception as e:
            bot.reply_to(message, f"Ошибка в команде:\n{e}")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
        else:
            bot.reply_to(message, answer)

        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)


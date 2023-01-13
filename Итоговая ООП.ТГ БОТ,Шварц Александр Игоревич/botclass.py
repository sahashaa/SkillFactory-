import requests  #импортируем для взаимодействия с API
import json  #Импортируем для перевода из JS в питон обьекты
from botconfig import *  #импортируем все из конфига

class APIexception(Exception):  #Наш класс исклчения
    pass

class Converter:  #класс производящий переводы
    @staticmethod
    def get_price(base, quote, amount):  #аргументы класса которые беруться от бота
        try:
            base_key = values[base.lower()]  #присваеваем начальной валюте перменную
        except KeyError:  #Отработка исключения если такого ключа не будет
            raise APIexception(f"Валюта {base} не найдена!")

        try:
            quote_key = values[quote.lower()]
        except KeyError:#Отработка исключения если такого ключа не будет
            raise APIexception(f"Валюта {quote} не найдена!")

        if base_key == quote_key:
            raise APIexception(f'Невозможно перевести {base} в {base}!')  #Отработка исключения если две валюты одинаковые

        try:
            amount = float(amount)
        except ValueError:
            raise APIexception(f'Не удалось обработать количество {amount}!')


        step1 = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}')#Отправка запроса апишке для получения словаря в джс
        step2 = json.loads(step1.content)#переводим из джс в питон обект
        step3 = step2[values[base.lower()]]*amount#делаем расчет
        step3 = round(step3, 3)
        etext = f"Цена {amount} {base} в {amount} : {step3}"
        return etext#результатом метода будет сам перевод

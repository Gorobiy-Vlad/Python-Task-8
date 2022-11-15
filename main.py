import requests as request
import cl_ExchangeRates as Rates
import datetime
import cl_Rogue as Rogue
import cl_Knight as Knight
import random

# 1.Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ),
# получите текущий курс валют и запишите его в TXT-файл

Rate_1 = Rates.Rates('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

# * 2.Пользователь вводит название валюты и дату,
# программа возвращает пользователю курс гривны к этой валюте за указаную дату используя API НБУ.
# Формат ввода пользователем данных - на ваше усмотрение. Реализовать с помощью ООП!


def Start():
    date = input("Enter Date (dd.mm.yyyy): ")
    try:
        if len(date[0:2]) == 2 and len(date[3:5]) == 2 and int(date[3:5]) < 12 \
                and len(date[6:]) == 4 and int(date[6:]) <= int(str(datetime.datetime.now())[0:4]):

            Rate_2 = Rates.Rates(f"https://bank.gov.ua/NBU_Exchange/exchange?json&date={date}")

        else:
            raise ValueError
    except ValueError:
        print("Error Date! ")
        print("*" * 100)

Start()
# ** 3.Для иры - создайте классы-наследники Unit :
#       Рыцарь (имеет 50% шанс нанести двойной урон цели)
#       Разбойник (имеет 50% шанс уклонится от урона противника)

Bob = Knight.Knight("Bob", 20, 15, 15)
Kane = Knight.Knight("Kane", 20, 20, 10)
Kane.Hit(Bob)
print("*" * 100)

Luci = Rogue.Rouge("Luci", 100, 10, 10)
Lina = Rogue.Rouge("Lina", 10, 20, 10)


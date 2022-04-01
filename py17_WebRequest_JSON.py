from urllib import request
import json
import time

url = "http://yand.dyndns.org/api/tickers.aspx"
print("My stock bot is on...")

previousValue = 0
# Непрерывный цикл опроса  url
while True:
    # Получение данных (текста) с url - всего одна строка
    result = request.urlopen(url).read().decode("utf-8")
    # print(result)
    stock = json.loads(result) # десериализация - очень здорово

    # print(stock)
    # for data in stock:
    #     print(f"Бумага {data['ticker']} текущий курс: {data['value']}")

    # реализация "сторожа", который следит за курсом ценной бумаги
    level = 1200
    for data in stock:
        if data['ticker'] == 'GAZPOM':
            currentValue = data['value']

            if currentValue > level and previousValue <= level:
                print(f"Текущий уровень: {currentValue}")

            if currentValue <= level:
                print(f"ДУМАЙ! текущий курс: {currentValue}")
            previousValue = currentValue

    time.sleep(1) # задержка на 1 сек





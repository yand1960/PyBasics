import json

# десериализация
f = open("data/tickers.json")
stock = json.load(f)
f.close()

# print(stock)
for data in stock:
    print(f"Бумага {data['ticker']} текущий курс: {data['value']}")


# сериализация

people = [
    {
    "firstName" : "Yuri",
    "lastName" : "Andrienko",
    "salary": 123456
    },

    {
    "firstName" : "Vasya",
    "lastName" : "Pupkin",
    "salary": 77777
    },

     {
    "firstName" : "Masha",
    "lastName" : "Mashkina",
    "salary": 300000
    },
]

f = open("data/people.json","w",encoding="utf-8")
json.dump(people,f)
f.close()

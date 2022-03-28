# Работа со списком строк

# people = ["Yuri", "Vasya", "Masha", "Yulia"]
# # for person in people:
# #     print(person)

# # Вывести все имена, которые начинаются на  Y
# # for person in people:
# #     if person[0] == "Y":
# #         print(person)

# # Вывести все имена, которые длиннее 4 букв
# for person in people:
#     if len(person) > 4:
#         print(person)

# Прдеставление сущность, обладающей несколькими атрибутами в виде списка
# person1 = "Yuri Andrienko 123456" # это не годится
# person1 = ["Yuri", "Andrienko", 123456]
# # Написать код, который выведет: "Y.Andrienko has salary 123456"
# print(f"{person1[0][0]}.{person1[1]} has salary {person1[2]}")

# Список списков = список сущностей, где каждая сущность предатвлена списком
# people = [
#      ["Yuri", "Andrienko", 123456],
#      ["Vasya", "Pupkin", 77777],
#      ["Masha", "Mashkina", 300000]
# ]

# for person in people:
#    print(f"{person[0][0]}.{person[1]} has salary {person[2]}") 

# # Найти и вывести фамилию самого высокооплачиваемого сотрудника
# richest = people[0]
# for person in people:
#     if person[2] > richest[2]:
#         richest = person
# print(f"Самый высокооплачиваемый - {richest[1]}")

# Представление сущности в виде словаря
# person = {
#     "firstName" : "Yuri",
#     "lastName" : "Andrienko",
#     "salary": 123456
# }
# print(f"{person['firstName'][0]}.{person['lastName']} has salary {person['salary']}")

# Список словарей
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

for person in people:
    print(f"{person['firstName'][0]}.{person['lastName']} has salary {person['salary']}")

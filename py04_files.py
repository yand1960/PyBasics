f = open("data/people.csv", encoding="utf-8")
text = f.read()
f.close()

# print(text)
lines = text.split("\n")
# print(lines)

#Разберите lines в тексты типа: "Yuri Andrienko has salary 123456"
# Способ 1. Разьираем лини текста для решения наших задач
# for line in lines:
#     # print(line)
#     splitted = line.split(";")
#     # print(splitted)
#     firstName = splitted[0]
#     lastName = splitted[1]
#     salary = splitted[2]
#     print(f"{firstName[0]}.{lastName} has salary {salary}")

 # Способ 2. Представляем содержащиеся данные файла 
 # в виде удобной для решения дальнейших задач структуры
people = []
for line in lines:
    # print(line)
    splitted = line.split(";")
    # print(splitted)
    firstName = splitted[0]
    lastName = splitted[1]
    salary = float(splitted[2])
    person = {"firstName": firstName, "lastName": lastName, "salary": salary}
    people.append(person)

#print(people)
# Вывести
# for person in people:
#     print(f"{person['firstName']} {person['lastName']} {person['salary']}")

# # Найти человека с макисмальной зарплатой
# richest = people[0]
# for person in people:
#     if person['salary'] > richest['salary']:
#         richest = person
# print(richest)

#  А что если максимальную заплату получают несколько людей?
people.append({'firstName':"Petya", 'lastName':'Petrov', 'salary': 300000})
# Сначала ищем макимальную зарплату 
maxSalary = 0
for person in people:
    if person['salary'] > maxSalary:
        maxSalary = person['salary']
print("Максимальная зарплата: " + str(maxSalary))
# Затем выводим всех людей с максимальной зарплатой
print("Список людей с максимальной зарплатой")
for person in people:
    if person['salary'] == maxSalary:
        print(f"{person['firstName']} {person['lastName']}")

# Вывести информацию о людях в другой файл в формате:
 #  Фамилия-табулятор-имя-табулятор-зарплата
f = open("data/people1.csv","w",encoding="utf-8")
for person in people:
    f.write(f"{person['lastName']}\t{person['firstName']}\t{person['salary']}\n")
f.close()

# Вывести информацию о самых высокооплачиваемых в третий файл в формате:
 #  Фамилия-табулятор-имя-табулятор-зарплата
f = open("data/people2.csv","w",encoding="utf-8")

for person in people:
    if person['salary'] == maxSalary:
        f.write(f"{person['lastName']}\t{person['firstName']}\t{person['salary']}\n")
f.close()



# print("Hello from VS Code!")

# Переменные, присвоения, числа
x = 2
x = (x + 1) * 123 / 456
print(x)

# Конкатенция строк, имена переменных
# s1 = "Yuri"
# s2 = 'Andrienko'
# # s3 = s1 + " " + s2
# s3 = f"{s1} {s2}"
# print(s3)

# firstName = "Yuri"
# lastName = "Andrienko"
# fullName = f"{firstName} {lastName}"
# print(fullName)

# Разборка строк + знакомство со списками
fullName = "Yuri Andrienko"
#  Способ 1
# spacePosition = fullName.find(" ")
# print(spacePosition)
# firstName = fullName[0:spacePosition] 
# lastName = fullName[spacePosition + 1:]
# print(firstName)
# print(lastName)

# Способ 2
# splitted = fullName.split(" ")
# # print(splitted)
# firstName = splitted[0]
# lastName = splitted[1]
# print(firstName)
# print(lastName)

# Ветвления (условный оператор)
# amount = 123
# if amount < 10:
#     print("Мало!")

# if amount >=10 and amount < 100:
#     print("В самый раз")

# if amount >= 100:
#     print("Многовато!")

# print("Анализ завершен")

# Вдруг в строке не оказалось пробела?
fullName = "Yuri Andrienko"
spacePosition = fullName.find(" ")
# print(spacePosition)
if spacePosition > 0:
    firstName = fullName[0:spacePosition] 
    lastName = fullName[spacePosition + 1:]
    print(firstName)
    print(lastName)
else:
    print(f"Не удалось разобрать строку {fullName}")







#  Очевидные манипулчции со списком:
data = [1, 2, 3, 333, 4, 2]
data.append(555)
data.pop(1)
# print(data)
# print(data[1])
# print(len(data))

# Перебор всех членов списка: оператор цикла
# Пронумеруем еще
# i = 1
# for x in data:
#     print(i, x)
    # i = i + 1
    # i += 1

# Сгенерируем новый список, в котором каждый член равен квадрату члена старого списка
# data2 = []
# for x in data:
#     data2.append(x * x)
# print(data2)

# Вывести из списка только те числа, которые больше 100
# for x in data:
#     if x > 100:
#         print(x)

# Вывести из списка только четные числа
# for x in data:
#     if x % 2 == 0:
#         print(x)

# Вывести из списка только те числа, которые больше 1000 или текст, что таких нет
# counter = 0
# for x in data:
#     if x > 1000:
#         print(x)
#         counter += 1

# if counter == 0:
#     print("Нет таких чисел!")

# Найти сумму всех чисел в списке
# sum = 0
# for x in data:
#     sum += x
# print(f"Сумма: {sum}")
# print(f"Среднее: {sum / len(data)}")

# Найти минимальное число в списке
min = data[0]
for x in data:
    if x < min:
        min = x
print(f"Минимальное: {min}")


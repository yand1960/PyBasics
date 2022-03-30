f = open("data/RusDictionary.txt", encoding="utf-8")
text = f.read()
f.close()

words = text.split("\n")
# print(words[0:100])

# Вывести из словаря все слова, которые начинаются на первые три буквы вашего имени
pattern = "юри"
# for w in words:
#     # if w[0:len(pattern)] == pattern:
#     #     print(w)

#     # if w.find(pattern) == 0:
#     #     print(w)

#     if w.startswith(pattern) :
#         print(w)

# # Вывести из словаря все слова, в которых содержатся первые три буквы вашего имени
# pattern = "юри"
# for w in words:
#     if w.find(pattern) >= 0:
#         print(w)  

# # Вывести из словаря все слова, которые заканчиваются на "цо"
# pattern = "цо"
# for w in words:
#     if w.endswith(pattern):
#         print(w)  

# Для каждого из этих паттернов вывести текст: <паттерн>: <число слов, которые на него начинаются>
patterns = ["але", "иго", "юри"]
for pattern in patterns:
    counter = 0
    for w in words:
        if w.startswith(pattern) :
            counter += 1
    print(f"{pattern}: {counter}")

# Найти самое длинное слово в русском языке
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
# print(longest, len(longest))
# Найти все самые длинные слова в русском языке
for w in words:
    if len(w) == len(longest):
        print(w)

# Еще немного о срезах
s = "qwertyuio"
print(s[1])
print(s[1:3])
print(s[1:])
print(s[1:7:2])
print(s[1::2])
print(s[::2])
print(s[-1])
print(s[::-1])
nums = [1,2,3,4,5,6]
print(nums[1:3])
print(nums[::-1])

# Найти в руском словаре все слова-перевертыши 
for w in words:
    if w == w[::-1] and len(w) > 1:
        print(w)

# Найти слова в русском языке, в которых больше всего букв л
pattern = "л"
# s = "лиллия"
# print(len(s.split(pattern)) - 1)

# maxPattern = 0
# for w in words:
#     if len(w.split(pattern)) - 1 > maxPattern:
#         maxPattern = len(w.split(pattern)) - 1
# print(maxPattern)

# for w in words:
#      if len(w.split(pattern)) - 1 == maxPattern:
#          print(w)

# Немного улучшим с точки зрения стуктуризации
# def countPattern(word, pattern):
#     return len(word.split(pattern)) - 1

def countPattern(word, pattern):
    counter = 0
    for letter in word:
        if letter == pattern:
            counter += 1
    return counter

pattern = "л"

maxPattern = 0
for w in words:
    if countPattern(w,pattern) > maxPattern:
        maxPattern =countPattern(w,pattern)
print(maxPattern)

for w in words:
     if countPattern(w,pattern) == maxPattern:
         print(w)

# Какая буква в каком слове русского языка встречается наибольшее число раз?
abc = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
bestWord = ""
bestLetter =  abc[0]
for pattern in abc:
    for w in words:
        if countPattern(w,pattern) > countPattern(bestWord, bestLetter):
            bestWord = w
            bestLetter = pattern
print(bestWord, bestLetter, countPattern(bestWord, bestLetter))


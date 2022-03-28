f = open("data/people.csv", encoding="utf-8")
text = f.read()
f.close()

# print(text)
lines = text.split("\n")
print(lines)

#Разберите lines в тексты типа: "Yuri Andrienko has salary 123456"
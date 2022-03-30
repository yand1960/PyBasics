from os import listdir

# Структурирование относительно сложного кода по млеким блокам

# ******* Укажите входную и выходную папки **************
IN_FOLDER = "data\\demo1"
OUT_FOLDER = "data\\demo1\\saved"
# ********************************************************

#  Эта функция отвечает за обработку единичного файла 
# (и вывод результатов обработки в выходной файл)
def processSingleFile(inFileName, f_out):
    f_in = open(f"{IN_FOLDER}/{file}", encoding="utf-8")
    text = f_in.read()
    f_in.close()
    lines = text.split("\n")
    for line in lines:
        splitted = line.split(" ")
        out = splitted[1] + ", " + splitted[0] + "\n"
        f_out.write(out)

# Этот блок кода отвечает за цикл по файлам
#  и за вызов функции обрботки еденечного файла
files = listdir(IN_FOLDER)
f_out = open(f"{IN_FOLDER}/people3.txt","w",encoding="utf-8")
for file in files:
    if file.find("data") >= 0:
        processSingleFile(file, f_out)
f_out.close()


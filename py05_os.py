import os

# ******* Укажите входную и выходную папки **************
IN_FOLDER = "data\\demo1"
OUT_FOLDER = "data\\demo1\\saved"
# ********************************************************

command = "calc"
# os.system(command)
# os.system("dir")

files = os.listdir(IN_FOLDER)
# print(files)
# Провести манипуляции только с файлами, в название которых есть data
# for file in files:
#     if file.find("data") >= 0:
#         # print(file)
#         command = f"copy {IN_FOLDER}\\{file} {OUT_FOLDER}\\{file}"
#         # print(command)
#         os.system(command)

# Из файлов data1.txt и data2.txt собрать данные в файл people3.txt
# в формате Фамилия, Имя
f_out = open(f"{IN_FOLDER}/people3.txt","w",encoding="utf-8")
for file in files:
    if file.find("data") >= 0:
        f_in = open(f"{IN_FOLDER}/{file}", encoding="utf-8")
        text = f_in.read()
        f_in.close()
        lines = text.split("\n")
        for line in lines:
            splitted = line.split(" ")
            out = splitted[1] + ", " + splitted[0] + "\n"
            # print(out)
            f_out.write(out)
f_out.close()

    





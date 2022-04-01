import pymssql
import os

# Опредедяем текущее имя экспортного файла
files  = os.listdir("data\export")
max = 0
for file in files:
    version = int(file.split("_")[1].replace(".csv",""))
    if version > max:
        max = version
max += 1
outputFile = f"data\\export\\products_{max}.csv"
print(outputFile)

# py -m pip install pymssql

# PATTERN = "Silver"
PATTERN = input("Введите буквы и нажмите ENTER: ")

connection = pymssql.connect(
    server="yand.dyndns.org",
    database = "AdventureWorks",
    user="northwind",
    password="northwind"
)

sql = f"""
    SELECT ProductID, Name,  ProductNumber, ListPrice
    FROM AdventureWorks.Production.Product
    WHERE Name LIKE '%{PATTERN}%'
"""

cursor = connection.cursor()
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
connection.close()

f = open(outputFile,"w")

print(f"{'id':5}\t{'name':35}\t{'code':10}\t{'price'}")
f.write("id,name,code,price\n")

# print(results)
for product in results:
    # print(product)
    id = product[0]
    name = product[1]
    code = product[2]
    price = product[3]
    print(f"{id:5}\t{name:35}\t{code:10}\t{price}")
    f.write(f"{id},{name},{code},{price}\n")

f.close()


os.system(f"start excel {outputFile}")
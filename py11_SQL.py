import pymssql

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

print(f"{'id':5}\t{'name':35}\t{'code':10}\t{'price'}")

# print(results)
for product in results:
    # print(product)
    id = product[0]
    name = product[1]
    code = product[2]
    price = product[3]
    print(f"{id:5}\t{name:35}\t{code:10}\t{price}")




# Написать код, который сформирует файл data\expensive.csv, 
# куда попадут товары ценой более 1000. Формат файла - решите сами
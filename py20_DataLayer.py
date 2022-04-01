import pymssql

class Repository:

    def getFilteredProducts(self, firstLetters):
        connection = pymssql.connect(
            server="yand.dyndns.org",
            database = "AdventureWorks",
            user="northwind",
            password="northwind"
        )

        sql = f"""
            SELECT ProductID, Name,  ProductNumber, ListPrice
            FROM AdventureWorks.Production.Product
            WHERE Name LIKE '{firstLetters}%'
        """

        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        products = []

        for product in results:
            # print(product)
            id = product[0]
            name = product[1]
            code = product[2]
            price = float(product[3])
            products.append(
                {
                    "id": id,
                    "name": name,
                    "code": code,
                    "price": price
                }
            )
        
        return products

if __name__ == "__main__":
    repository = Repository()
    print(repository.getFilteredProducts("a"))
        


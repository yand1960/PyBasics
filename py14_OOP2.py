# Это типичный класс. Для него валидно понятие объекта (=экземпляр класса)
class MyGeometry:

    # Это называется конструктор класса. 
    # Он вызывается, когда создается экземпляр класса
    # Cлово self в заголовке конструктора 
    # - это скорее маркер принадлежности объекту, чем аргумент функции
    def __init__(self):
        #  Это называется поле [экземпляра] класса (не совсем точно - свойство)
        self.noneuqluid = 1.0

    # Это называется метод [экземпляра] класса
    def hypot(self,a, b):
        c = (a * a + b * b) ** 0.5 * self.noneuqluid
        return c

    def square(self, a, b):
        return a * b / 2 * self.noneuqluid

if __name__ == "__main__":
    # Создаем экземпляр(ы) нужного класса
    g1 = MyGeometry()
  
    g2 = MyGeometry()
    g2.noneuqluid = 1.1
    g3 = MyGeometry()
    g3.noneuqluid = 0.9
    print(g1.hypot(3,4), g2.hypot(3,4), g3.hypot(3,4))


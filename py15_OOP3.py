from py14_OOP2 import MyGeometry

class MyGeometryExtended(MyGeometry):
    
    def cathet(self,a,c):
        return (c * c - a * a) ** 0.5 * self.noneuqluid


if __name__ == "__main__":
    ge1 = MyGeometryExtended()
    print(ge1.hypot(3,4), ge1.cathet(4,5))
    print(ge1.__str__())
    print(ge1)
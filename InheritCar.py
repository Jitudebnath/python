class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class BMWcar(car):
    def __init__(self,name):
        self.name=name

car1= BMWcar("m5 limited edition")
car2= BMWcar("m4 special edition") 

print(car1.start())
print(car2.stop())
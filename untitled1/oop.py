class Man:
    def __init__(self):
        self.tooth = 32
    def getInfo(self):
        return "You have {} tooth".format(self.tooth)
class Child(Man):
    def __init__(self):
        self.tooth = 28
class Crocodile(Child):
    def __init__(self):
        self.animal = True
        super().__init__()
    def isAnimai(self):
        return self.animal
    def getInfo(self):
        print(super().getInfo()+".\nIs ", end="")
        if self.animal:
            print("animal!")
        else:
            print("not animal!")


I = Man()
You = Child()
She = Crocodile()
print(I.getInfo())
print(You.getInfo())
She.getInfo()

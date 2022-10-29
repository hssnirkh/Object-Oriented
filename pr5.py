
class Test():
    five = 5
    def addFive(self,num):
        num = num +self.five
        return num
x = Test()
x.five = 10
print(x.addFive(100))
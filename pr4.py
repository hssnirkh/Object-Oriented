#private value in class not printed

class Test():
    __num = 20
    def __showMessage():
        print("hello")

x = Test()
print(x.__showMessage)
print(x.__num)

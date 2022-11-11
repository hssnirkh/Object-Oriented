import random
list1 =[]
from tokenize import Name
#1
class person :
    def __init__(self, n = "", a = "", c = 0):
        self.__name = n
        self.__lastname = a
        self.__ucode = c

    def Ucode(self):
        return self.__name

    def Ucode(self, value):
        self.__name = value

    def Name(self):
        return self.__name

    def Name(self, value):
        self.__name = value


    def Lastname(self):
        return self.__lastname

    def Lastname(self, value):
        self.__lastname = value
#2
    def Crand ():
        list1 = []
        for i in range (1,10):
            print(random.randint(1,10))
            list1.append(random.randint(1,10))
            
#4
class Child(person):
    def __init__(self, n = "", a = ""):
        super().__init__(n, a)

    def Crand():
        list2 =[]
        for i in range (1, 10):
            print(random.random())
            list1.append(random.random())
            list2.append(random.random())


#6
class Grandchild(Child):
    #7
    def __init__(self, n = "", a = ""):
        super().__init__(n, a)

    def Capital(self):
        t =str (self.Name.upper())
        v =str(self.Lastname.upper())
        h=t+v
        print(h)
        file = open ("C:\\Users\ROG\\Desktop\\sample.txt.txt","w")
        file.write(h[::-1])

person.Crand()
Child.Crand()
Person1 = Grandchild()
Person1.Name = "armita"
Person1.Lastname = "jvnd"
Person1.Capital()
person2 = person ()
person3 = person()
person4= person()

list=[]
for i in range(0,10):
    person1 = person()
    list.append(person1)


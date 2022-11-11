#Amirreza Zarei
#python 21
import random
#1
class Person:
    __ucode = 0
    __name = "No Name"
    __lastname = "No Lastname"
#3
    def __init__(self):
        self.__ucode
        self.__name
        self.__lastname

#3

    def Name(self):
        return self.__name
    def Name(self, value):
        self.__name = value



    def Ucode(self):
        return self.__ucode
    def Ucode(self, value):
        self.__ucode = value


    def Lastname(self):
        return self.__lastname
    def Lastname(self, value):
        self.__lastname = value

#2

    def crand(self):
        list1 = []
        list2 = []
        for i in range(1,10):
            list1.append(random.randint(1,10))
        for i in list1:
            if i not in list2:
                list2.append(i)
        self.Ucode = random.sample(list2,1)

#4

class Child(Person):
#5
    def __init__(self):
        super().__init__()

#4

    def crand(self):
        list3 = []
        list3.append(random.random())
        print(list3)

#6
#7
class Grandchild(Child):
    def __init__(self):
        super().__init__()
    
#6
#9
    def capital(self, n, l):
        file = open("C:\\Users\\Shiraz 1\\Desktop\\Exam.txt", "w")
        file.write(n[::-1].upper() + l[::-1].upper())
        file.close()

#8
list4=[]
for i in range(0,10):
    personx = Person()
    list4.append(personx)

for i in list4:
    i.crand()
    if (i.Ucode[0]%2 == 0):
        list4.remove(i)

person1 = Grandchild()
person1.Name = "amir"
person1.Lastname = "zarei"
person1.capital(person1.Name, person1.Lastname)
person1.crand()


    


    
    




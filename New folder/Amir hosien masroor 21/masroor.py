#Amirhosien Masroor
#group 21 of python

import random
#import for use random tabe

#1

class Person:
    __name   = "no name"
    __lastname = "no last name"
    __ucode  = 0

#3

    def __init__(self):
        self.__name  
        self.__lastname
        self.__ucode

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, value):
        self.__name = value
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter    
    def lastname(self, value):
        self.__lastname = value

    def Ucode(self):
        return self.__ucode
    def Ucode(self, value):
        self.__ucode = value

#2

    
    def Random(self):
        list1 = []
        list2 = []
        for i in range(1,10):
            list1.append(random.randint(1,10))
        for i in list1:
            if i not in list2:
                list2.append(i)
        self.Ucode = random.sample(list2,1)
        print(self.Ucode)
        return
        

#4

class Child(Person):

#5

    def __init__(self):
        super().__init__()

    def Random(self):
        list3 = [] 
        for i in range(1,10):
            print(random.random())

#6

class GrandChild(Child):

#7

    def __init__(self,n,ln):
        super().__init__()
        self.__name = n
        self.__lastname = ln
        
    def Capital(self):
        a = self.__name
        b = self.__lastname
        c = a.upper()+b.upper()
        print(c)

#9

        d = c[::-1]
        file = open("C:\\Users\\Lenovo\\Desktop\\Amirhosien Masroor.txt" , "w")
        file.write(d)
        file.close()
        
person1=Person()
person1.Random()
child=Child()
random.Random()
grandchild=GrandChild("amirhosien","masroor")
grandchild.Capital()

#8

listx=[]
for i in range(0,10):
    personx = Person()
    listx.append(personx)

for i in listx:
    i.Random()
    if (i.Ucode[0]%2 == 0):
        listx.remove(i)

#10(comment well done)
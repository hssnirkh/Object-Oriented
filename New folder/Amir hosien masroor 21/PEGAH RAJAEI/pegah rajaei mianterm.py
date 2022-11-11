#pegah 
#rajaei
#GP 17 python

import random
#1
class Person:
    __name   = ""
    __family = ""
    __ucode  = 0
    #3
    def __init__(self):
        self.__name  
        self.__family
        self.__ucode

    def Name(self):
        return self.__name
    def Name(self, value):
        self.__name = value

    def Family(self):
        return self.__family
    def Family(self, value):
        self.__family = value

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
 #       print(self.Ucode)
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
    def __init__(self,n,f):
        super().__init__()
        self.__name = n
        self.__family = f
        
    def Capital(self):
        a = self.__name
        b = self.__family
        c = a.upper()+b.upper()
        print(c)
        #9
        d = c[::-1]
        file = open("C:\\Users\\ALLAHQOQNUS\\Desktop","+w")
        file.write(d)
        file.close()
        
person=Person()
person.Random()
child=Child()
child.Random()
grandchild=GrandChild("Pegah","rajaei")
grandchild.Capital()

#8
#create an object list
list=[]
for i in range(0,10):
    personx = Person()
    list.append(personx)
print(list)
print()
print()
#remove even ucode
for i in list:
    i.Random()
    if (i.Ucode[0]%2 == 0):
        list.remove (i)
print(list)

    



    
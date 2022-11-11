#mohammad hassani 21
import random
#1
#3
class person:
    __name = "no name"
    __familyname = "no familyname"

    def __init__(self):
        self.__name
        self.__familyname


    
    def name(self):
        return self.__name
    def name(self, value):
        self.__name = value
   
    def familyname(self):
        return self.__familyname
    def familyname(self, value):
        return self.__familyname
   #2 
    def crand(self):
        list1 = []
        list1.append(random.random())
        peint(list1)
        for i in range(0, len(list1)):
            if (list1[i] % 2 ==0):
                list1.remove(list1[i])
        print(list1)
    
#4
#5
class child(person):
    def __init__(self):
        super().__init__()
#8
def crand(self):
    list1=[]
    list1.append(random.random())
    print(list1)
    for i in range(0, len(list1)):
        if (list1[i] %2 == 0):
            list.remove(list1[i])
        print(list1)
#6 
#7       
class grandchild(child):
    def __init__(self):
        super().__init__()
#9       
        def capital(self, h, l):
            file=open("C:\Users\ADMIN\Desktop\mohammadhassani", "w")
            file.write(n[::-1].upper() + l[::-1].upper())
            file.close()


person1 = grandchild()
person1.name = "gholi"
person1.familyname = "rastegar"
person1.capital(person1.name, person1.familyname)
person1.crand

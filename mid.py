#Hassan Irankhah
import random

class Person():
    __name = ""
    __family = ""
    randNum = []

    def __init__(self):
        self.__name
        self.__family
    
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value

    @property
    def Family(self):
        return self.__name
    @Family.setter
    def Family(self,value):
        self.__family = value

    def crand(self):
        pList = []
        for i in range(1,11):
            num = random.randint(1,1000)
            pList.append(num)
        randNum = random.sample(pList, 1)
        return randNum

class Child(Person):
    def __init__(self):
        super().__init__()
    
    def crand(self):
        chList = []
        for i in range(1,11):
            chList.append(random.random())
        return chList

class GrandChild(Child):
    def __init__(self):
        super().__init__()

    def display(self): 
        str1 = self.Name
        str2 = self.Family
        st = str1+str2
        stRev = st[::-1]
        return stRev

#creating objects
person1=Person()
person2=Child()
print(person1.crand())
print()

print(person2.crand())
print()

person3=GrandChild()
person3.Name="Hassan"
person3.Family="Irankhah" 
print(person3.display())
person3.display()

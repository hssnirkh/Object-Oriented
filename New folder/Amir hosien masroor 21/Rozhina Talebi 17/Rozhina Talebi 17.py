#ROZHINA Talebi/ 17 py
import random
#1
class Person:
    __name   = "NO name"
    __family = "No lastname"
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
        print(self.Ucode)
        
        
#4
class child(Person):
    def __init__(self, name, lastname, z):
        super().crand(n) 
        print(randnom.random())
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
        file = open("C:\\Users\\Asus\\Desktop\\EXAMMMM", "+w")
        file.write(d)
        file.close()
        
person=Person()
person.Random()
child=Child()
child.Random()
grandchild=GrandChild("Rozhina","Talebi")
grandchild.Capital()            
            




#8
list1 = []
class Person:
    def __init__(self,name,lastname,z):
        self.__name = "none"
        self.__lastname= "none"
        self.z = n
        list1.append(n)
        if(n%2 == 0):
            list.remove(n)        


        
        
        
    

            
            
            
            
            

        
        
        
        
        
        
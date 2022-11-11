#fatemeh zahiremami/python17
#2
import random
#1
#3:self,init
class Person:

    def __init__(self,name,lastname,a):
        self.__name = ""
        self.__lastname= ""
        self.a = b
        
    def Name(self):
        return self.__name


    def Name(self,value):
        self.__name = value
    
    def Lastname(self):
        return self.__lastname

    def Lastname(self,value):
        self.__lastname = value 
        
    
#2 Edame
    def crand(b):
        Ucode=[]
        for i in range(1,11):
            b = random.sample(i,1)
            Ucode.append(b)
#8
                        
            if(b%2 == 0):
                Ucode.remove(b)            
            return b





#4
class Child(Person):
#5:self,init
    def __init__(self, name, lastname, a):
        super().crand(b) 
        print(randnom.random(0,1))   
    def showmessage(self):
        print("num:{0}".format(self. super().crand(b)))   

    
#6    
class grand(Child , Person):
    
        name2  = str(input("Enter your name:"))
        lastname2 = str(input("Enter your lastname: ")) 
        lastname2 = lastname2.strip()
        name2 = name2.strip()
        print(name2.upper()+lastname2.upper())
#9    
        v = (name2.upper()+lastname2.upper())
        u = v[::-1]
        file = open("C:\\Users\\public20\\Desktop\\fatemeh zahiremami py17\\exam.txt", "+w")
        file.write(u)
        file.close()
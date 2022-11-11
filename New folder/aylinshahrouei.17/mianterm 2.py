#Aylinshahrouei

#1
import random
class Person:
    
    __name= ""
    __lastname = ""
    
    def __init__(self):
        self.__name
        self.__lastname
        
    def Name(self):
        return self.__name
    def Name(self, value):
        self.__name = value
        
    def Lastname(self):
        return self.__lastname
    def Lastname(self, value):
        self.__lastname = value    
        
        
    def showinfo(self):
        print("name :{0}".format(self.name))
        print("last name :{0}".format(self.lastname))
        
firstperson = Person()
firstperson.name = "aylin"
firstperson.lastname="shahrouei"
firstperson.showinfo()


#2
def crand(self):
    adad = 0
    list = []
    list.append(adad)
    for i in range(1, 10):
        print(random.random())
def showinfo(self):
    print("adad: {0}.".format(self.adad))
crand = Person()
crand.showinfo
#3
class Person1:
    
    def __init__(self, n= " ",a = 0,h =0):
        self.name  = n
        self.age   = a
        self.hight = h       
    
    def showinfo1(self):
        print("name :{0}".format(self.name))
        print("age :{0}".format(self.age))
        print("height :{0}".format(self.height))
        
firstperson1 = Person1()
firstperson1.name = "aylin"
firstperson1.age=17
firstperson1.height = 175
firstperson1.showinfo1()

#4
class parent:
    def __init__(self):
        print("parent Constructor!")
        
class Child(parent):
    def __init__(self):
        print("Child Constructor!")
        super().__init__()
 
myChild = Child()
crand.showinfo

#5
class Parent:  
    def __init__(self, m):
        self.message = m


    def Message(self):
        return self.message


    def Message (self, value):
        self.message = value

    def showmessage (self):
        print(self.message)

class Child(Parent):
    def __init__(self, m):
        super().__init__(m)

myParent = Parent("Message from parent.")
myChild  = Child("Message from child.")

myParent.showmessage ()
myChild.showmessage ()

myParent.Message = "Modified message of the parent."
myParent.showmessage ()
#6
class Parent:
    def __init__(self, m):
        self.message = m

    def Message(self):
        return self.message

    def Message (self, value):
        self.message = value
    def upercase(self):
        esm = "aylin"
        family = "shahrouei"
        print(esm.upper()+family.upper())

    def showmessage (self):
        print(self.message)

class Child(Parent):
    def __init__(self, m):
        super().__init__(m)

class GrandChild(Child):
    def __init__(self, m):
        super().__init__(m)      

myParent     = Parent("Message from parent.")
myChild      = Child("Message from child.")
myGrandChild = GrandChild("Message from GrandChild.")

myParent.showmessage ()
myChild.showmessage ()

print()

myParent.Message = "Modified message of the parent."
myParent.showmessage ()

myChild.Message  = "Modified message of the child."
myChild.showmessage ()

print(myParent.upercase())

#7
class Parent:
    def __init__(self, m):
        self.message = m

    def Message(self):
        return self.message

    def Message (self, value):
        self.message = value

    def showmessage (self):
        print(self.message)

class Child(Parent):
    def __init__(self, m):
        super().__init__(m)

class GrandChild(Child):
    def __init__(self, m):
        super().__init__(m)

myParent     = Parent("Message from parent.")
myChild      = Child("Message from child.")
myGrandChild = GrandChild("Message from GrandChild.")

myParent.showmessage ()
myChild.showmessage ()

print()

myParent.Message = "Modified message of the parent."
myParent.showmessage ()

myChild.Message  = "Modified message of the child."
myChild.showmessage ()

#8
list[]
list=Person
list.append(list)

for i in range(1,11):
    if(list[i] %2==0):
        list.remove(list[i])
        
#9
d = c[::-1]
file = open("C:\\Users\\RSco\\Desktop\\exam.txt","w")
file.write(d)
file.close()
    
Person=Person()
Person.Random()
Child=Child()
Child.Random()
GrandChild=GrandChild("aylin","shahrouei")
GrandChild.Capital()




























        

        
        


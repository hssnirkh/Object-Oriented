#foroozan/python17
#1
class Person:
    __name=" "
    __lastname=" "
    def __init__(self):
        self.__name
        self.__lastname
        
    def Name(self):
        return self.__name


    def Name(self,value):
        self.__name = value
    
    def Lastname(self):
        return self.__lastname

    def Lastname(self,value):
        self.__lastname = value 

person1 = Person()
person1.Name  ="Foroozan"
person1.Lastname  ="bita"
print("name : {0}".format(person1.Name))
print("lastname : {0}".format(person1.Lastname))

#2
def Crand(self):
    Ucode=[]
    for i in range(1,11):
        x=random.randit(1,11)
        Ucode.append(x)
        y=random.sample(Ucode,1)

    return y

def Showinformation(self):
    print("num:".format(self.Crand))
mynumber=Person()
#mynumber.Showinformation()

#3

def _init_(self, a="",b =""):
        self.name = a
        self.lastname = b

def showmesssage(self):
    print("name :{0}".format(self.name))
    print("lastname :{0}".format(self.lastname))


firstperson1 = Person()
firstperson1.name="foroozan"
firstperson1.lastname="bita"
firstperson1.showmessage()


#4
class Child(Person):
    def __init__(self):
        super().__init__()
    def Crand(self):
        Ucode=[]
        for i in range(1,11):
            x=random.randit(0,1)
            Ucode.append(x)
            return Ucode
    def Showinformation2(self):
        print("listcrand={0}".format(self.Crand))
    
mychild=Child()
mychild.Showinformation2()

#5
class Parent:
    def __init__(self,n):
        self.message = n

        def Message(self):
            return self.message

        def Message(self,value):
            self.message = value
            
        def showmessage(self):
            print(self.message)
            
class Child(Parent):
    def __init__(self,n):
        super().__init__(n)

myParent.showmessage()
myChild.showmessage()

myParent.Message = "msge of the parent."
myParent.showmessage()
    
#6    
class grand(Child , Person):
        name2  = str(input("Enter your name:"))
        lastname2 = str(input("Enter your lastname: ")) 
        lastname2 = lastname2.strip()
        name2 = name2.strip()
        print(name2.upper()+lastname2.upper())

#7
class Parent:
    def __init__(self,n):
        self.message = n

    def Message(self):
        return self.message
    def Message(self,value):
        self.message = value
    def showmessage(self):
        print(self.message)
        
class Child(Parent):
    def __init__(self,n):
        super().__init__(n)

myParent = Parent("Msg from parent.")
myChild  = Child("msg from child.")
myGrandChild = GrandChild("Msg from GrandChild.")

myParent.showmessage()
myChild.showmessage()

print()

myParent.Message = "msg of the parent."
myParent.showmessage()

myChild.Message = "msg of the child."
myChild.showmessage()        
#8

list11 = Person()

list1.append(list11)

for i in range(1,11):
    if(list1[i].crand[i]%2==0):
        list1.remove(list1[i])
        
#9    
        v = (name2.upper()+lastname2.upper())
        u = v[::-1]
        file = open("C:\\Users\\Soheilrayan\\Desktop\\Exam.txt", "+w")
        file.write(u)
        file.close()

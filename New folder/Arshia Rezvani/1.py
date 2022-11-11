#Arshia
#Rezvani
#grpup 17 py
import random
#1
class person:
    __name=""
    __lastname=""
    __ucode=0
    #3
    def __init__(self):
        self.__name
        self.__lastname
        self.__ucode=0

    def Name(self):
        return self.__name
    def Name(self,value):
        self.__name=value
    def Name(self):
        del self.__name

    def Lastname(self):
        return self.__lastname
    def Lastname(self,value):
        self.__name=value
    def Lastname(self):
        del self.__name

    def Ucode(self):
        return self.__ucode
    def Ucode(self,value):
        self.__ucode=value
    def Ucode(self):
        del self.__ucode
        
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
#       print(self.Ucode)

#4
class child(person):
    def __init__(self):
        super().__init__()

    def Random(self):
        list3 = [] 
        for i in range(1,10):
            print(random.random())


#6
class Grandchild(child):
   #7
    def __init__(self,x,y):
        super().__init__()
        self.__name=x
        self.__lastname=y


    #def totitlecase(person):
        #words=list(person.split(""))
        #for i in range(0,len(words)):
            #firstletter=words[i][0:1]
            #rest=words[i][1:]
            #result=firstletter.upper()+rest.lower()
            #words[i]=result  
        #return str.join("",words)  
    def Capital(self):
        a = self.__name
        b = self.__lastname
        c = a.upper()+b.upper()
        print(c)
        #9
        d = c[::-1]
        file = open("C:\\Users\\Nik\\Desktop\\giii.txt","w")
        file.write(d)
        file.close()
#8
list=[]
for i in range(0,10):
    personi = person()
    list.append(personi)
print(list)

for i in list:
    i.Random()
    if (i.Ucode[0]%2 == 0):
        list.remove(i)
print(list)

person1=person()
mychild=child()
person.random()
child.random()
person.Name=input("Enter your first name:\n")
person.Lastname=input("Enter your last name:\n")
print("name:{0}" .format(person1.Name))
print("Lastname:{0}" .format(person1.Lastname))


        


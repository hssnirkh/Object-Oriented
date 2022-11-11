#seyed Ehsan Hosseini
#py 21
#midterm2
import random
#1
class Person:
    __name=""
    __family="" 
    ucode=[]
           
    def __init__(self):
        pass
        
            
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name=value

    @property
    def Family(self):
        return self.__family
    @Family.setter
    def Family(self,value):
        self.__family=value     

#2
    def crand(self):
    
        list=[]
        for i in range(1,11):    
            number=random.randint(1,1000)
            list.append(number)
            
        ucode=random.sample(list,1)
        
        return ucode           
            
#soal4,5
class Child(Person):
    def __init__(self):
        super().__init__()
        
#4      
    def crand(self):
        b=[]
        for i in range(1,11):
            b.append(random.random())
        return b
    
#soal6,7
class GrandChild(Child):
    def __init__(self):
        super().__init__()
#6        
    def showinfo(self): 
        str1=self.Name
        str2=self.Family
        str_total=str1+str2

        return str_total.upper()
        
        
        
#creating objects
person11=Person()
person12=Child()
print(person11.crand())
print()

print(person12.crand())
print()

person13=GrandChild()
person13.Name="hassan"
person13.Family="irankhah" 
print(person13.showinfo())
print()



#8
f=[]
y=[]
for i in range(1,11):
    S="person"+str(i)
    S=Person()
    f.append(S)
     
for i in f:
    X=i.crand() 
    if(X[0]%2==0):
        f.remove(i)
    else:
        y.append(X[0])

print(y)    
    
   

#9
g=list(person13.showinfo())
g.reverse()
info_rev="".join(g)

file= open("exam.txt","w")
file.write(info_rev)
file.close()
    

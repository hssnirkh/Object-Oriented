#Iman Hosseini
#midterm
import random

#1
class Person:
    __name=""
    __family="" 
    ucode=[]
           
#3
    def __init__(self):
        pass
        
            
    def Name(self):                 # property
        return self.__name
    
    def Name(self,value):           # Name.setter
        self.__name=value

    
    def Family(self):               # property
        return self.__family
    
    def Family(self,value):         # Family.setter
        self.__family=value     

#2
    def crand(self):
    
        list=[]
        for i in range(1,11):    
            number=random.randint(1,1000)
            list.append(number)
            
        ucode=random.sample(list,1)
        
        return ucode           
            
# question 4 , 5

class Child(Person):
    def __init__(self):
        super().__init__()
        
#4      
    def crand(self):
        g=[]
        for i in range(1,11):
            g.append(random.random())
        return g
    
# Question 6,7
class GrandChild(Child):
    def __init__(self):
        super().__init__()
#6        
    def information(self):
        str1=self.Name
        str2=self.Family
        result=str1+str2
        return result.upper()
          
#objects

person11=Person()
person12=Child()
print(person11.crand())
print()

print(person12.crand())
print()

person13=GrandChild()
person13.Name="hassan"
person13.Family="irankahh"
print(person13.information())
print()

#8
list1=[]
list2=[]
for i in range(1,11):
    S="person"+str(i)
    S=Person()
    list1.append(S)

print(list1)
     
for i in list1:
    X=i.crand()
    if(X[0]%2==0):
        list1.remove(i)
    else:
        list2.append(X[0])

print(list2)
    

#9
g=list(person13.information())
g.reverse()
info_rev="".join(g)

file= open("t.txt","w")
file.write(info_rev)
file.close()
#Hassan Irankhah
import random

#1
class Person:
    __name=""
    __family="" 
    ucode=[]
           
#3
    def __init__(self):
        #pass
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
        return self.__family
    @Family.setter
    def Family(self,value):
        self.__family = value

#2
    def crand(self):

        mainList=[]
        for i in range(1,11):
            number=random.randint(1,1000)
            mainList.append(number)

        ucode=random.sample(mainList,1)
        return ucode

#4 , 5

class Child(Person):
    def __init__(self):      # 5
        super().__init__()

#4
    def crand(self):
        ranNum=[]
        for i in range(1,11):
            ranNum.append(random.random())
        return ranNum

#6 
class GrandChild(Child):
    def __init__(self):    #7
        super().__init__()
#6        
    def display(self):
        s1=self.Name
        s2=self.Family
        sum=s1+s2
        return sum.upper()
          
#instance
print("crand from #2:")
p1=Person()
print(p1.crand())

print("crand from #4:")
p2=Child()
print(p2.crand())

print("Upper Name:")
p3=GrandChild()
p3.Name="hassan"
p3.Family="irankhah"
print(p3.display())
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

g=list(p3.display())
g.reverse()
rev="".join(g)

file= open("Exam.txt","w")
file.write(rev)
file.close()

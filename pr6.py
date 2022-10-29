#Encapsulation
class Persion_Enc():
    #privat property
    __name = "no name"
    __age = 0
    __id = 0
    #constructor
    def __init__(self):
        self.__name
        self.__age
        self.__id
    #getter
    @property
    def Name(self):
        return self.__name
    #setter
    @Name.setter
    def Name(self,value):
        self.__name = value
    #deleter optional
    def Name(self):
        del self.__name
    @property
    def AGG(self):
        return self.__age
    @AGG.setter
    def AGG(self,value):
        self.__age = value
    @AGG.deleter
    def AGG(self):
        del self.__age
    @property
    def Ident(self):
        return self.__id
    @Ident.setter
    def Ident(self,value):
        self.__id = value
    




p = Persion_Enc()
p.Name = "hassan"
p.AGG = 30
p.Ident = 229
print(p.Name,p.AGG,p.Ident)

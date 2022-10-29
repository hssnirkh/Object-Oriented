class CarSale():
    __brand = "no brand"
    __model = "0"
    __color = "no color"
    __createYear = 0

    def __init__(self):
        self.__brand
        self.__model
        self.__color
        self.__createYear
    
    def showCar(self):
        print(self.BRD,self.MDL,self.CLR,self.CY)

    
    @property
    def BRD(self):
        return self.__brand
    @BRD.setter
    def BRD(self,value):
        self.__brand = value

    @property
    def MDL(self):
        return self.__model
    @MDL.setter
    def MDL(self,value):
        self.__model = value

    @property
    def CLR(self):
        return self.__color
    @CLR.setter
    def CLR(self,value):
        self.__color = value
    
    @property
    def CY(self):
        return self.__createYear
    @CY.setter
    def CY(self,value):
        self.__createYear = value



car1 = CarSale()
car1.BRD = "ford"
car1.MDL = "mustang"
car1.CLR = "red"
car1.CY = 1971

car1.showCar()
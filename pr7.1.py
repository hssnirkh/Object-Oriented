class CarSale():
    def __init__(self,__brand = "no brand",__model = "0",__color = "no color",__createYear = 0):
        self.__brand = __brand
        self.__model = __model
        self.__color = __color
        self.__createYear = __createYear
    
    def showCar(self):
        print(f"Brand={self.BRD} ",f"model={self.MDL} ",f"Color={self.CLR} ",f"Year={self.CY} ")
    

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
class CarBuy(CarSale):
    def ifAvalable(self):
        if(super().BRD == "shevrollet"):
            print("ford is avalable")
        else:
            print(super().BRD)
        
car1 = CarSale()
car1.BRD = "ford"
car1.MDL = "mustang"
car1.CLR = "red"
car1.CY = 1971

car1.showCar()
car2 = CarSale("shevrollet","camaro SS","green",1978)
car2.showCar()

car3 = CarBuy("peraid","131","white",2008)
car3.ifAvalable()
car3.showCar()


class Persion:
	def __init__(self,name="",id=0,age=0):
		self.name = name
		self.id = id
		self.age = age
	def printValue(self):
		print(f"name : {self.name}")
		print(f"id : {self.id}")
		print(f"age : {self.age}")
fPersion = Persion("hassan",222,30)
fPersion.printValue()
sPersion = Persion("reza")
sPersion.printValue()
tPersion = Persion("",222)
tPersion.printValue()
fPersion = Persion("asghar","",21)
fPersion.printValue()

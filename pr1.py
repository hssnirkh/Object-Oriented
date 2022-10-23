#no init
class Persion:
	name = ""
	id = 0
	age = 0
	#diplay
	def showPersion(self):
		print(f"name : {self.name}")
		print(f"id : {self.id}")
		print(f"age : {self.age}")

firstPersion = Persion()
firstPersion.name = input("enter name : ")
firstPersion.id = int(input("enter id : "))
firstPersion.age = int(input("enter age : "))
firstPersion.showPersion()

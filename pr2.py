#constructor --init--
class Persion:
	def __init__(self,n="",i=0,a=0):
		self.name = n
		self.id = i
		self.age = a
	def display(self):
		print(f"Name : {self.name}")
		print(f"Id : {self.id}")
		print(f"Age : {self.age}")

firstPersion = Persion(input("name:"),int(input("id:")),int(input("age:")))
print()
firstPersion.display()
print(type(firstPersion))
print(type(Persion))
print(Persion.n)
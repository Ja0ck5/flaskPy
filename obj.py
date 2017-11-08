#coding=utf-8
class Dog:

	# __color = 'white' # private 
	color = 'white'
	gender = 'male'

	def setName(self,name):
		self.name = name
		# self.__money = 1000000000.00 # private 

	def eat(self):
		print("%sI'm eating..."%self.name)

	def run(self):
		print("I'm running...")


d1 = Dog()
d1.setName("test1")
d1.eat()

print(d1.color)
print(d1.gender)
print(d1.name)
print(d1.money)
d2 = Dog()
d2.setName("test2")
d2.eat()

d3 = Dog()
d3.setName("test3")
d3.run()
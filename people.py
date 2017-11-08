#coding=utf-8
class People:

	__name = "Tom"

	__age = 12
	# 构造方法
	def __init__(self):
		print('this is a constructor...')

	def __del__(self):
		print 'now done...'	


	def getName(self):
		return self.__name

	# private # def __getName(self):
		# return self.__name

	def getAge(self):
		return self.__age
	
	def printName(self):
		print 'name:',self.__name

def myPrint(p):
	p.printName()		

p = People()
#del p
myPrint(p)
print p.getName,p.getAge


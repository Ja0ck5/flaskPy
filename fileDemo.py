#coding=utf-8
import os

# f = open('D:/f.txt','w')
# f = open('D:/f.txt','r')
# f.write('Hello world,Who am I')

# content = f.read(3)

# print(content)

# content= f.readlines()

# print(type(content))
# for temp in content :
# 	print(temp)
# f.close()

# content = f.read(10)

# while len(content)>0 :
# 	print(content)	
# 	content = f.read(0)

# f.close()
# oldFileName = 'D:/f.txt'
# oldFile = open(oldFileName,'r')


# num = oldFileName.rfind('.')

# left = oldFileName[0:num]
# right = oldFileName[num:]

# newFile = open(left +'-copy' + right,'w')

# content = oldFile.readline()
# print(content)
# while len(content)>0 :
# 	newFile.write(content)
# 	content = oldFile.readline()


# oldFile.close()
# newFile.close()

fileName = 'D:/f.txt'
# f = open(fileName,'r')

# position = f.tell()

# print "当前位置：" , position

# f.seek(5,0) #var1:offset ,var2: 0: 文件开头;1:当前位置;2:文件末尾

# print(f.read(5))
# position = f.tell()
# print "当前位置：" , position

# f.close()


# os.rename(fileName,fileName+'---rename')

# movieNames = os.listdir('D:/data')
# for movieName in movieNames:
# 	print(movieName)

# os.remove(fileName)

# os.mkdir('D:/testMkdir')

# currentDir = os.getcwd()
# print(currentDir)

# listDir = os.listdir(currentDir)
# for tmp in listDir:
# 	print(tmp)


try:
	print(num)
# except Exception as e:
	# raise
	# print("this is an exception",e)
# except NameError as ne:
# 	print('this is a nameError',ne)
# except IOError as ie:		
# 	print('this is an IOError',ie)
# except (NameError,IOError) as e :
# 	print('this is an error',e)
except (NameError,IOError) , result :
	print('this is an error',result)
else:
	pass
finally:
	# pass
	print('I am the finally')

import testImport

testImport.printSomething()

from testImport import printSomething
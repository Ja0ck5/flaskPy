# coding=utf-8
class ShortInputException(Exception):
    '''定义的异常类'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Please enter.....')

    if len(s) < 3:
        # raise 引发一个异常
        raise ShortInputException(len(s),3)

except EOFError:
    print '/n U input an end token EOF'
except ShortInputException,x: # x 变量被绑定到了错误的实例
    print('ShortInputException: length %d,length at least %d'%(x.length,x.atleast))
else:
    print 'nothing happen....'
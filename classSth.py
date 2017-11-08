# coding=utf-8
class Man:
    # 类属性
    age = 100

    def __init__(self):
        self.num = 20

    # 类方法
    @classmethod
    def setAge(cls, age):
        cls.age = age

    @staticmethod
    def staticSetAge():
        print 'static set age'


man = Man()
Man.age = 10
man.setAge(200)

print(man.num)
print(man.age)

man2 = Man()

print man2.age

Man.staticSetAge()

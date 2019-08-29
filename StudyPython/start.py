if __name__ == "__main__":
    print('start')

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b
'''
end 关键字
关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

'''

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a + b
#
# for letter in 'Runoob':  # 第一个实例
#     if letter == 'b':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
#
# print("Good bye!")

# for i in [1, 0]:
#     print(i)
#     print(i+1)


# import sys  # 引入 sys 模块
#
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# numbers = [1, 3, 6]
# newNumbers = tuple(map(lambda x: x, numbers))
# print(newNumbers)

# a = [66.25, 333, 335, 1, 1234.5]
# b = [1, 2, 3]
#
# a.extend(b)
# print(a)

# a.insert(2, -1)
# a.remove(333)
# a.reverse()
# a.sort()
# print(a)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]
#
# print(matrix)
#
# result = [[row[i] for row in matrix] for i in range(4)]
#
# print(result)

# one = []
# for x in range(4):
#     print(x)
#     one.append([row[x] for row in matrix])
#     print(one)
#     pass
# print(one)

# import support

# 现在可以调用模块里包含的函数了
# support.print_func("Runoob")
#
# str = input("请输入：");
# print("你输入的内容是: ", str)

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


# import pprint, pickle
#
# # 使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()


# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())

# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
#
#
# x = Complex(3.0, -4.5)
# print(x.r, x.i)  # 输出结果：3.0 -4.5

# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
#
# t = Test()
# t.prt()

# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 实例化类
# p = people('runoob', 10, 30)
# p.speak()
#

# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
# s = student('ken', 10, 60, 3)
# s.speak()


# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
#
#
# # 多重继承
# class sample(speaker, student):
#     a = ''
#
#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
#
#
# test = sample("Tim", 25, 80, 4, "Python")
# test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
# super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
#

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# x.__foo()  # 报错

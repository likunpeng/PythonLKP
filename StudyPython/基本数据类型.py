if __name__ == '__main__':
    print("基本数据类型")

# counter = 100  # 整型变量
# miles = 1000.0  # 浮点型变量
# name = "run oob"  # 字符串
#
# print(counter)
# print(miles)
# print(name)


# listArr = ['abc', 786, 2.23, 'runOob', 70.2]
# tinyList = [123, 'run oob']
#
# print(listArr)  # 输出完整列表
# print(listArr[0])  # 输出列表第一个元素
# print(listArr[1:3])  # 从第二个开始输出到第三个元素
# print(listArr[2:])  # 输出从第三个元素开始的所有元素
# print(tinyList * 2)  # 输出两次列表
# print(listArr + tinyList)  # 连接列表


# def reverse_words(input_str):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     input_words = input_str.split(" ")
#     print(input_words)
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     input_words = input_words[-1::-1]
#     print(input_words)
#     # 重新组合字符串
#     output = ' '.join(input_words)
#
#     return output
#
#
# if __name__ == "__main__":
#     input_str = 'I like runLoop'
#     rw = reverse_words(input_str)
#     print(rw)

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[0:3:2])
# print(t[-1])
# print(t[-1::-1])
#
# print(t[4::-1])

"""
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

注意：

1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法一样。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用+操作符进行拼接。

"""
# print("tuple")
#
# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
#
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号
#
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
# print(tuple[2:])  # 输出从第三个元素开始的所有元素
# print(tinytuple * 2)  # 输出两次元组
# print(tuple + tinytuple)  # 连接元组
# print(tuple[-1::-1])

''''
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
'''

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
#
# print(student)  # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if 'Rose' in student:
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)  # a 和 b 的差集
#
# print(a | b)  # a 和 b 的并集
#
# print(a & b)  # a 和 b 的交集
#
# print(a ^ b)  # a 和 b 中不同时存在的元素

'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。

'''
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值


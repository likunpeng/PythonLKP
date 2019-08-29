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

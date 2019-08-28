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

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x, numbers))
print(newNumbers)

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

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[0:3:2])
print(t[-1])
print(t[-1::-1])
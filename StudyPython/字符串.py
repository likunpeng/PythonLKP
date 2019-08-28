if __name__ == "__main__":
    print('字符串')

# var1 = 'Hello World!'
# var2 = "Runoob"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])
#
# print("已更新字符串 : ", var1[:6] + 'Runoob!')


a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

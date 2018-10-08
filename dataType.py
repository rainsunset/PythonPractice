# 数据类型
# 整数 范围:任意大小
#     - 10进制：1 0 -1的·
#     - 16进制：0xffoo
#     - arithmetic operation
print(1+1)
print(1-2)
print(1*2)
# Python2会输出整数 Python3会输出小数
print(3/2)
print(3 ** 2)
print((2+3)*4)
# 浮点数 
#     - 数学写法：1.23 ,-9.01
#     - 科学记数法：1.23e9 ,1.2e-5
#     - 浮点数运算 但是 计算结果包含的小数是不准确的
print(0.2+0.1)
print(0.2-0.1)
print(3*0.1)
print(0.3/2)
# str()函数
num = 7
print("I'd like number" + str(num) +",and you ?")
# 字符串
#     - 单引号 或 双引号包围
#     - 转义符 \  \n \t \\
print('Languages:\n\tPython\n\tJava\n\tJavaScript')
#     - r'' 表示内部字符不转义
#     - '''...'''可表示多行内容 ... 为提示符，不是代码一部分
print('''line1
line2
line3''')
#     - Change Case
message = 'this is title'
print(message.title())
print(message.upper())
print(message.lower())
#      - string builder
first_name = 'Li'
last_name = 'GangWei'
full_name = first_name + ' ' + last_name
print('Hello, ' + full_name.title() + ' !')
#     - remove blank
blank_word = '  Hello world  '
print('|'+blank_word+'|')
no_blank_word1 = blank_word.rstrip()
print('|'+no_blank_word1+'|')
no_blank_word2 = blank_word.lstrip()
print('|'+no_blank_word2+'|')
no_blank_word3 = blank_word.strip()
print('|'+no_blank_word3+'|')
# 布尔值
#     -True
#     -False
#     -也可以是计算值
print(3 < 2)
#     -也包含运算符
#     -and or not
print(not(True and False))
# 空值 None
# 列表
# 字典
# 自定义数据类型
# 变量
#     - 变量名必须是大小写英文、数字和_(下划线)的组合 且泵用数字开头
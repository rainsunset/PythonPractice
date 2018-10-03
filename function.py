#encoding: utf-8
# 函数 python 是区分大小写的
# 规则: 冒号结尾 下一行的缩进视为代码块
# 约定4个空格为1个缩进  不能用tab
print('输入整数。。。。')
a = input()
if int(a) >= 0:
	print(a)
else:
	print(-int(a))

# 数据类型
# 整数 范围:任意大小
#     - 10进制：1 0 -1的·
#     - 16进制：0xffoo
# 浮点数 
#     - 数学写法：1.23 ,-9.01
#     - 科学记数法：1.23e9 ,1.2e-5
# 字符串
#     - 单引号 或 双引号包围
#     - 转义符 \  \n \t \\
#     - r'' 表示内部字符不转义
#     - '''...'''可表示多行内容 ... 为提示符，不是代码一部分
print('''line1
line2
line3''')
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
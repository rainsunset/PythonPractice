# coding:utf-8
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
print(r'D:\MyGitCode\PythonPractice')
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
# 字符替换
strs = "cat1cat3cat3"
print(strs.replace("cat","dog"))
print(strs)
# 字符分割
str1 = ("If by life you were deceived, Don't be dismal,don't be wild! In the "
        + "day of grief,be mild: Merry days will come,believe. Heart is living "
        + "in tomorrow; Present is dejected here: In a moment,passes sorrow; "
        + "That which passes will be dear.")
# 分割单词
worlds = str1.split()
num_words = len(worlds)
print("字符串包含单词数" + str(num_words))
sentence = str1.split(",")
print(sentence)
sentence = str1.split(",",2)
print(sentence)
# 字符串格式化（Python使用一个字符串作为模板。模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。
# Python用一个tuple将多个值传递给模板，每个值对应一个格式符。）
# 格式符
# %s    字符串 (采用str()的显示)    %r    字符串 (采用repr()的显示)
# %c    单个字符                   %b    二进制整数
# %d    十进制整数                 %i    十进制整数
# %o    八进制整数                 %x    十六进制整数
# %e    指数 (基底写为e)           %E    指数 (基底写为E)
# %f    浮点数                     %F    浮点数，与上相同
# %g    指数(e)或浮点数 (根据显示长度) %G    指数(E)或浮点数 (根据显示长度)
# %%    字符"%"
print("I'm %s. I'm %d year old" % ('Vamei', 99))
# 进一步格式化
# %[(name)][flags][width].[precision]typecode
# (name)为命名
# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
# width表示显示宽度
# precision表示小数点后精度
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
# 上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：
print("%.*f" % (4, 1.2))
# Python实际上用4来替换*。所以实际的模板为"%.4f"。

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
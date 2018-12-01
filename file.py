# encoding:utf-8

filepath = 'pi_digits.txt'
# 读取整个文件 
with open(filepath) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

# win下文件路径使用反斜杠\ linux和osx中使用斜杠/
# ？？ python 获取当前操作系统

# 逐行读取文件
with open(filepath) as file_object:
	for line in file_object:
		print(line.rstrip())

# 读取文件到列表
with open(filepath) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

# 使用文件内容
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print(float(pi_string))

# 读取大文件
big_file_path = "file/pi_million_digits.txt"
with open(big_file_path) as big_file_object:
	big_lines = big_file_object.readlines()
big_pi_string = ''
for line in big_lines:
	big_pi_string += line.strip()
print(big_pi_string[:52]+"...")
print(len(big_pi_string))

# 检查文件中包含特定值
while True:
	birthday = input("输入你的生日(纯数字)")
	if birthday in big_pi_string:
		print("生日被包含")
	else:
		print("未被包含")
	isout = input("是否继续测试，退出请输入no，其他任意键继续")
	if isout.lower() == "no":
		break

# 写入文件
big_file_path_copy = "file/pi_million_digits_copy.txt"
with open(big_file_path_copy,'w') as file_copy:
	file_copy.write(big_pi_string)
with open(big_file_path_copy) as file_copy:
	lines_copy = file_copy.readlines()
pi_string_copy = ''
for line in lines_copy:
	pi_string_copy += line.strip()
print(len(pi_string_copy))
# with语句可以更容易地清理打开的文件 
# open 函数默认'r' 只读模式
# 'w' 时，若文件不存在 python将创建文件 若文件已存在python将先清空文件内容再返回
# 'r+' 读取和写入文件模式
# 'a' 附加模式(追加内容)
# 'b' 附加说明某模式用于二进制文件 比如'rb' 'wb'
# 'U' 通用换行模式，单独使用或附加到其他读模式， 如'rU'
# python 只能将字符串写入到文本中，写入数字时要用str()转义

# 写入多行
with open(big_file_path_copy,'w') as file_copy:
	with open(big_file_path) as big_file_object:
		for line in big_file_object:
			file_copy.write(line.strip() + '\n')

# 附加模式
guest_file = "file/guest_file.txt"
with open(guest_file,'a') as guest_file_obj:
    while True:
	    message = input("随便输点儿啥，内容将会被追加,输exit退出输入")
	    if message.strip() == "exit":
	    	break
	    else:
	    	guest_file_obj.write(message)
with open(guest_file) as guest_file_obj:
	print("刚输入的内容:\n------ 开始 ------")
	for line in guest_file_obj:
		print(line.strip())
	print("------ 结束 ------")

# 使用多个文件
# 使用函数实现
from file_util import count_words
filenames = ["dataType.py","hello.py","list.py","aaaayy.txt",guest_file,big_file_path_copy]
words_count = 0
for filename in filenames:
	words_count += count_words(filename)
print(str(len(filenames))+"个文件的单词总量为"+str(words_count))

# 使用json存储数据  读取json
import json

number = [2,3,5,76,12,90,23,1]
number_filename = 'number.json'
with open(number_filename,'w') as f_obj:
	json.dump(number,f_obj)
with open(number_filename) as f_obj:
	number = json.load(f_obj)
print(number)

uname_filename = 'uname.json'
try:
	with open(uname_filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError as e1:
	username = input("你是谁？")
	with open(uname_filename,'w') as f_obj:
		json.dump(username,f_obj)
		print("你退出再回来试试")
except Exception as e:
	print("未知异常")
else:
	print(username + "欢迎你回来!")
# ?? 写进去是unicode码  汉字就不会正常显示了，，解决一下？？

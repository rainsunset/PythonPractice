try:
	print(5/0)
except ZeroDivisionError:
	print("异常 -- 除数不能为0")

# try- excert - else
while True:
	first_number = input("请输入被除数，摁q退出\n")
	if first_number == "q":
		break
	second_number = input("请输入除数\n")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError as e:
		print("异常 -- 除数不能为0")
	except ValueError as e1:
		print("输入有误 -- 请输入数字")
	else:
		print(answer)

# FileNotFoundError
filename = 'aaased.txt'
try:
    with open(filename) as f_proj:
	    content = f_proj.read()
except FileNotFoundError as e:
	print(filename + "文件不存在")
else:
	print("搞么子 快把文件删了")

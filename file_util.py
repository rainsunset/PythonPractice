# encoding:utf-8
def count_words(filename):
	""" 计算一个文件大致包含多少个单词 """
	num_words = 0
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError as e1:
		print("文件" + filename + "不存在")
	except Exception as e:
		print("解析文件"+filename+"发生未知异常")
	else:
		# 计算文件包含了多少个单词
		words = contents.split()
		num_words = len(words)
		print("文件:"+filename+"单词数为:"+str(num_words))
	return num_words
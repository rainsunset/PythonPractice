# encoding:utf-8
def get_formatter_name(first,last,middle=''):
	"""格式化名字"""
	if middle == '':
		full_name = first + ' ' + last
	else:
		full_name = first + ' ' + middle + ' ' + last
	return full_name.title()
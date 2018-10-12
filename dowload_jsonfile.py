# coding:utf-8

# urllib urlopen 方式读取网络json文件
from __future__ import (absolute_import,division,print_function,unicode_literals)
try:
	# python2.*版本
	from urllib2 import urlopen
except Exception as e:
	# python3.*版本
	from urllib.request import urlopen
import json
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
# 读取数据
req_urllib = response.read()
# 将数据写入文件
with open("file/btc_close_2017_urllib.json","wb") as urllib_file:
	urllib_file.write(req_urllib)
# 加载json格式
# file_urllib = json.loads(req_urllib)
file_urllib = json.loads(req_urllib.decode('utf8'))
print(file_urllib)

# requests方式读取网络文件
import requests
req_requests = requests.get(json_url)
# 将数据写入文件
with open("file/btc_close_2017_request.json","w") as requests_file:
	requests_file.write(req_requests.text)
file_request = req_requests.json()
print(file_request)

print(file_urllib == file_request)
# 保存后两个文件内容一致，但是
# btc_close_2017_request.json 43K 
# btc_close_2017_urllib.json41k
# 何解？？？


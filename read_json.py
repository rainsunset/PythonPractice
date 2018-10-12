# coding:utf-8
import json
import pygal
import math

filename = "file/btc_close_2017.json"
with open(filename) as f_obj:
	json_data = json.load(f_obj)
# 逐条打印
dates = []
months = []
weeks = []
weekdays = []
closes = []
for item in json_data:
	# print(item)
	date = item['date']
	month = int(item['month'])
	week = int(item['week'])
	weekday = item['weekday']
	close = int(float(item['close']))
	# item_str = '{} is month {} week {},{},the close price is {}RMB '.format(date,month,week,weekday,close)
	# print(item_str)
	dates.append(date)
	months.append(month)
	weeks.append(week)
	weekdays.append(weekday)
	closes.append(close)
# 绘制图表
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价',closes)
line_chart.render_to_file('收盘价折线图(￥).svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(x) for x in closes]
line_chart.add('收盘价',closes_log)
line_chart.render_to_file('收盘价对数变换折线图(￥).svg')

# 封装计算平均值的函数
from itertools import groupby
def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        # 注意:此处x轴的值必须为str类型
        xy_map.append([str(x),sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'收盘价月日均值(￥)',
    '月日均值')
# line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值(￥)',
	'周日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday']
weekday_int = [(wd.index(w) +1) for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekday_int, closes[1:idx_week],'收盘价星期均值(￥)',
	'星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('收盘价星期均值(￥).svg')

# 数据仪表盘
with open('收盘价Dashboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html>\n<head>\n<title>收盘价Dsahboard</title>\n<meta charset="utf8">\n</head>\n<body>\n')
    for svg in ['收盘价折线图(￥).svg','收盘价对数变换折线图(￥).svg','收盘价月日均值(￥).svg',
                '收盘价周日均值(￥).svg','收盘价星期均值(￥).svg']:
        html_file.write('<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
    html_file.write('</body></html>')
# encoding:utf-8
import pygal
from random_walk import RandomWolk

# 不断模拟随机漫步
i = 0
while True:
	rw = RandomWolk(10000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	group_list = [(rw.x_values[value],rw.y_values[value]) for value in range(len(rw.x_values))]

	xy_chart = pygal.XY(stroke=False)
	xy_chart.title = '随机漫步'
	xy_chart.add('漫步者',group_list)
	filename = "random_walk" + str(i) + ".svg"
	i = i + 1
	xy_chart.render_to_file(filename)	
	# 继续执行？？
	keep_running = input('再来一次?(y/n)')
	if keep_running.strip() == 'n':
		break
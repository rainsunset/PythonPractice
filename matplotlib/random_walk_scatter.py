# encoding:utf-8
import matplotlib.pyplot as plt
from random_walk import RandomWolk

# 不断模拟随机漫步
while True:
	rw = RandomWolk(10000)
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, s=10, c=point_numbers, cmap=plt.cm.BuGn, edgecolors='none')
	# 着重标记首尾
	plt.scatter(0, 0, c='Blue', edgecolors='none', s=50)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Red', edgecolors='none', s=50)
	# plt.title('随机漫步', fontsize=20)
	# plt.xlabel('X方向', fontsize=14)
	# plt.ylabel('Y方向', fontsize=14)
	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	# 这个适配没啥用呢？？？
	plt.Figure(dpi=72,figsize=(16,2))
	plt.savefig("random_walk.png")
	plt.show()
	keep_running = input('再来一次?(y/n)')
	if keep_running.strip() == 'n':
		break
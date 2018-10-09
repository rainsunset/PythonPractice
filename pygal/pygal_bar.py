# encoding:utf-8
from die import Die
import pygal

# 创建一个六面骰子和10面骰子
die6 = Die()
die10 = Die(10)
# 随机掷n次 求和
results = [((die6.roll() + die10.roll())) for value in range(5000)]
x_values = list(range(2,17))
# 分析结果
frequencies = [results.count(value) for value in x_values]

# 可视化结果
hist = pygal.Bar()
hist.title = "D6 And D10"
hist.x_labels = [str(value) for value in x_values]
hist.x_title = "点数"
hist.y_title = "次数"
hist.add('D6 + D10',frequencies)
hist.render_to_file('dice_visual.svg')
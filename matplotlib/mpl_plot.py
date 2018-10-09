# encoding:utf-8

import matplotlib.pyplot as plt

input_value = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]
# 线宽
plt.plot(input_value,squares,linewidth=3)
# 设置标题及xy轴标签 字体
plt.title("square number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
# 设置标记刻度大小
plt.tick_params(axis="both",labelsize=8)

plt.show()

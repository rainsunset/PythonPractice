# encoding:utf-8

import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5,6]
# y_values = [1,4,9,16,25,36]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values,y_values,s=10,edgecolors='none',c='red')
# plt.scatter(x_values,y_values,s=10,edgecolors='none',c=(0,0,0.8))
plt.scatter(x_values,y_values,s=10,edgecolors='none',c=y_values,cmap=plt.cm.YlOrBr)
plt.title("scatter test")
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
# 设置坐标轴区间
plt.axis([0,1000,0,1100000])
plt.tick_params(axis="both",which="major",labelsize=14)
# 保存图像 一定要放在show之前
# plt.savefig("mpl_csatter_img.png",bbox_inches='tight')
plt.show()

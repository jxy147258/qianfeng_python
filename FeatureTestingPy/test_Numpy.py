import numpy as np
from matplotlib import pyplot as plt

# 直线图
# x = np.arange(1, 10)
# y = x * 2 + 5
# plt.title('test for NumPy')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x, y, 'xk')
# plt.show()

# 正弦图和两个图并存
# x = np.arange(0, 3 * np.pi, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.subplot(2, 3, 1)
# plt.plot(x, y1, 'xk')
# plt.title('test for NumPy_sin') # 区别于只有一个表的情况，两个表的时候不能有x，y坐标的lable函数
#
# plt.subplot(3, 2, 2)
# plt.plot(x, y2, 'ob')
# plt.title('test for NumPy_cos')
#
# plt.show()

# 直方图
# x = [5, 8, 10]
# y = [12,16,6]
# x2 = [6,9,11]
# y2 = [6,15,7]
# plt.bar(x, y, align='center')
# plt.bar(x2, y2, color='g', align='center')
# plt.title('Bar graph')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()


x1 = np.arange(1, 11)
y = 2 + x1 + x1 * x1 + x1 * x1 * x1

plt.title('user defined diagram')
plt.plot(x1, y)
plt.show()

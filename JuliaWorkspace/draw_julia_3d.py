#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use("svg")

# 定义一个函数来计算朱利亚集
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# 定义复平面的参数
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

# 创建图像的像素网格
width, height = 800, 800
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)

# 创建3D坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义复常数c的变化范围和步长
c_imag_min, c_imag_max = -1.5, 1.5
c_real = 0.285  # 固定复常数的实部，选择一个产生有趣图案的值

# 计算朱利亚集的迭代次数
mandelbrot_set = np.vectorize(mandelbrot)
iterations = mandelbrot_set(X + 1j * Y, 50)

# 将迭代次数转换为三维点云
Z = iterations.copy()
Z[iterations == 0] = 0  # 将未逃逸的点设置为NaN以在图中去除

# 绘制三维点云图
scatter = ax.scatter(X, Y, Z, c=iterations, cmap='hot', marker='.')

# 添加色彩条
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Iterations')

# 设置坐标轴标签
ax.set_xlabel('Re(Z)')
ax.set_ylabel('Im(Z)')
ax.set_zlabel('Im(c)')

# 设置图表标题
ax.set_title('3D Julia Set')

# 显示图表
# plt.show()
plt.savefig("output/julia_3d.svg")

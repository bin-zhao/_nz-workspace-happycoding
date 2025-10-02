#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

# 选择一个复常数c
c = complex(-0.8, 0.156)

# 计算朱利亚集的迭代次数
mandelbrot_set = np.vectorize(mandelbrot)
iterations = mandelbrot_set(X + 1j * Y, 100)

# 将迭代次数转换为热图
plt.imshow(iterations, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')

# 优化显示效果
plt.colorbar()
plt.title('Julia Set')
plt.xlabel('Re(Z)')
plt.ylabel('Im(Z)')
plt.grid(False)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# 显示图表
plt.savefig("output/julia.svg")
# plt.show()

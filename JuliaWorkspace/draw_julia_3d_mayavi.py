#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import mayavi.mlab as mlab

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

# 定义复常数c的变化范围
c_imag_min, c_imag_max = -1.5, 1.5
c_real = 0.285  # 固定复常数的实部

# 计算朱利亚集的迭代次数
mandelbrot_set = np.vectorize(mandelbrot)
iterations = mandelbrot_set(X + 1j * Y, 100)

# 将迭代次数转换为三维点云
Z = np.zeros(iterations.shape)
for imag_c in np.linspace(c_imag_min, c_imag_max, height):
    Z += iterations * (imag_c - c_imag_min)

# 绘制三维点云图
mlab.figure(size=(800, 800))
mlab.points3d(X, Y, Z, scale_factor=0.1, colormap='hot')

# 添加色彩条
# mlab.colorbar()

# 设置图表标题
mlab.title('3D Julia Set')

# 显示图表
mlab.show()

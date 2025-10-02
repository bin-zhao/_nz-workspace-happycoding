#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")

z_value = 0

ax.plot_surface(
    np.linspace(-2, 2, 100),
    np.linspace(-2, 2, 100),
    np.full((100, 100), z_value),
    color="b",
    alpha=0.3
)

complex_points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
x, y = zip(*complex_points)
z = [z_value] * len(x)

ax.scatter(x, y, z, color="red")

ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.set_zlabel("Z (constant)")

ax.set_title("Complex Plane in 3D Space")

ax.grid(True)

plt.show()

'''
plt.figure(figsize=(8, 8))
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(color="lightgray", linestyle="--")

plt.scatter(x_part, y_part, color="red")

plt.annotate("", xy=(1.2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
plt.annotate("", xy=(0, 1.2), xytext=(0, 0), arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.title("Complex Plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")

plt.show()
'''

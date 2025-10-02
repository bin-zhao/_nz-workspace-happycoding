#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

image_size = 4096
max_iter = 100

x = np.linspace(-2, 1, image_size)
y = np.linspace(-1.5, 1.5, image_size)
X, Y = np.meshgrid(x, y)

C = X + 1j * Y

img = np.zeros((image_size, image_size))

for i in range(max_iter):
    diverged = np.abs(C) > 2

    C[diverged] = 0
    C[~diverged] = C[~diverged]**2 + X[~diverged] + 1j * Y[~diverged]

    img[diverged] = i

img = img / max_iter

plt.imshow(img, extent=[-2, 1, -1.5, 1.5], cmap="hot")
plt.colorbar()

plt.title("Mandelbrot Set")
plt.xlabel("Re(C)")
plt.ylabel("Im(C)")

plt.show()

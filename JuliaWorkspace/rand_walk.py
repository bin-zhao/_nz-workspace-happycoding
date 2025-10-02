#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import random
import matplotlib.pyplot as plt
import numpy as np

CUR_DIR = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))

def rand_test(count):
    p = [0, 0]
    for _ in range(count):
        rx = np.random.randint(0, 2)
        ry = np.random.randint(0, 2)
        if rx == 0:
            p[0] -= 1
        elif rx == 1:
            p[0] += 1
        if ry == 0:
            p[1] -= 1
        elif ry == 1:
            p[1] += 1
    return p

def main():
    np.random.seed()

    count = 1000
    x_list = []
    y_list = []
    for _ in range(10000):
        p = rand_test(count)
        x_list.append(p[0])
        y_list.append(p[1])

    plt.scatter(x_list, y_list, s=1)
    fig, ax = plt.subplots(tight_layout=True)
    ax.hist2d(x_list, y_list)
    plt.show()

main()
print("done!")

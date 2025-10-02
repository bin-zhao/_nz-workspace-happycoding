#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import quad
import math

def f(x):
    return 1 / np.floor(x) - 1 / x
    # return 1 / (1 + x) - math.pow(np.e, -x) / x

# Numerical derivative
x = np.linspace(0, 2, 100)
y = f(x)
dy = np.gradient(y, x)

# Numerical integration from 0 to 2
result, error = quad(f, 1, 100000)
print("Result:", result)

def main():
    pass

main()
print("done!")

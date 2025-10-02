#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import symbols

def main():
    x, y, z = symbols("x y z")
    print(type(x))
    print(dir(x))
    print(x, y, z)

main()
print("done!")

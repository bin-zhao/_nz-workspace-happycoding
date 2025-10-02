#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import random
 
def main():
    count = 100
    a = 0
    b = 0
    x_list = []
    for i in range(0, count):
        x = random.randint(0, 1)
        x_list.append(x)
        if x == 0:
            a += 1
        else:
            b += 1

    print(", ".join([str(it) for it in x_list]))

    print("a: %.8f" % (float(a) / count))
    print("b: %.8f" % (float(b) / count))


    print("done!")

main()

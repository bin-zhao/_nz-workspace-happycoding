#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def main():
    A = np.array([
        [2, 4, -1, 5],
        [-4, -5, 3, -8],
        [2, -5, -4, 1],
        [-6, 0, 7, -3]
    ])

    A = np.random.uniform(1, 10000, (4, 4))

    # Q, _ = np.linalg.qr(A)
    # A = Q

    print(A)
    print(np.linalg.cond(A))

    A_inv = np.linalg.inv(A)
    print(A_inv)
    print(A @ A_inv)
    print(A_inv @ A)

main()
print("done!")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

if False:
    import numpy as np
    import matplotlib.pyplot as plt

    # 创建网格
    x, y = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

    # 定义电场
    Ex = -x / (np.sqrt(x**2 + y**2) + 1e-9)
    Ey = -y / (np.sqrt(x**2 + y**2) + 1e-9)

    # 绘制向量场
    plt.quiver(x, y, Ex, Ey)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Electric Field')
    plt.show()


if False:
    import numpy as np
    import matplotlib.pyplot as plt

    # 创建网格
    x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

    # 定义速度场
    vx = -y
    vy = x

    # 绘制向量场
    plt.quiver(x, y, vx, vy)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Velocity Field')
    plt.show()

if False:
    import numpy as np
    import matplotlib.pyplot as plt

    # 创建网格
    x, y = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

    # 定义引力场
    Gx = -x / (np.sqrt(x**2 + y**2) + 1e-9)
    Gy = -y / (np.sqrt(x**2 + y**2) + 1e-9)

    # 绘制向量场
    plt.quiver(x, y, Gx, Gy)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gravitational Field')
    plt.show()

if True:
    import numpy as np
    import matplotlib.pyplot as plt

    # 创建网格
    x, y = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))

    # 定义热流场
    qx = -x
    qy = -y

    # 绘制向量场
    plt.quiver(x, y, qx, qy)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Heat Flux Field')
    plt.show()

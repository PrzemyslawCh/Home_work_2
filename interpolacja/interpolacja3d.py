# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:22:40 2020

@author: user
"""

import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

# tworzymy punkty na osiach x i y
x = np.arange(-6, 6, 1.5)
y = np.arange(-6, 6, 1.5)

# tworzymy siatkę punktów na płaszczyźnie xy
X, Y = np.meshgrid(x, y)

plt.plot(X, Y, 'o')

# wyliczamy Z dla każdego punktu siatki
Z = np.sin(np.sqrt(X**2+Y**2))

fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,rstride=1, cstride=1,
                cmap='autumn', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 35)

plt.show()


# INTERPOLACJA


f = interp2d(x, y, Z, kind='linear')

xx = np.arange(-6, 6, 0.1)
yy = np.arange(-6, 6, 0.1)

XX, YY = np.meshgrid(xx, yy)

#plt.plot(XX, YY, 'o')

ZZ = f(xx, yy)

fig2 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(XX, YY, ZZ,rstride=1, cstride=1,
                cmap='autumn', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(60, 35)

plt.show()
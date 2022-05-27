import math
import scipy
import numpy as np
from scipy import linalg


from numpy.core import umath
from scipy.interpolate import interp1d
from scipy.interpolate import pchip_interpolate
import matplotlib.pyplot as plt

# Funkcje pomocnicze

def f1(x, y):
    return x ** 2 + y ** 2 - 4


def f2(x, y):
    return x ** 2 - y + 2


def f1x(x):
    return 2 * x


def f1y(y):
    return 2 * y


def f2x(x):
    return 2 * x


def f2y():
    return -1

###### Rysowanie wykresów ######

# tworzymy punkty na osiach x i y
x = np.arange(-6, 6, 1.5)
y = np.arange(-6, 6, 1.5)
# tworzymy siatkę punktów na płaszczyźnie xy
X, Y = np.meshgrid(x, y)
# wyliczamy Z dla każdego punktu siatki
Z = X ** 2 + y ** 2 - 4
Z2 = X ** 2 - Y + 2
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,rstride=1, cstride=1,
                cmap='autumn', edgecolor='none')
ax.plot_surface(X, Y, Z2,rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(60, 35)
plt.show()

def Chachaj_Przemyslaw_Newton_wielowymiarowy(x, y, eps):
    xk = np.array([[x], [y]], dtype='float64')
    # print(xk)
    jac = np.matrix([[f1x(xk[0]), f1y(xk[1])], [f2x(xk[0]), f2y()]], dtype='float64')
    revjac = linalg.inv(jac)
    # print(revjac)
    fxk = np.array([[f1(xk[0][0], xk[1][0])], [f2(xk[0][0], xk[1][0])]], dtype='float64')
    # print(fxk)
    # print(revjac.dot(fxk))
    g = revjac.dot(fxk)
    xkp = xk -g
    # print(xkp)
    ax.scatter3D(xkp[0][0], xkp[1][0], Z, c=Z, cmap='Greens')
    
    while (np.linalg.norm(xkp - xk) > eps):
        xk = xkp
        jac = np.matrix([[f1x(xk[0]), f1y(xk[1])], [f2x(xk[0]), f2y()]], dtype='float64')
        # print(jac)
        revjac = linalg.inv(np.matrix(jac))
        # print(revjac)
        fxk = np.array([[f1(xk[0][0], xk[1][0])], [f2(xk[0][0], xk[1][0])]], dtype='float64')
        xkp = np.subtract(xk, (revjac.dot(fxk)))
        # print(xkp)
        ax.scatter3D(xkp[0][0], xkp[1][0], Z, c=Z, cmap='Greens')

    x = xkp

    return x

print(Chachaj_Przemyslaw_Newton_wielowymiarowy(1, 1, 0.1))


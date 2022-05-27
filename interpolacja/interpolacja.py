# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:13:52 2020

@author: user
"""

import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import pchip_interpolate
import matplotlib.pyplot as plt

# WEZLY INTERPOLACYJNE
x = np.linspace(0, 2, 7)
x = x*np.pi
y = np.sin(x)

# Punkty, w których wyliczamy wartosci funkcji interpolacyjnych
x2 = np.linspace(0, 2, 1000)
x2 = x2*np.pi

# FUNKCJE SCHODKOWE

f_1 = interp1d(x, y, kind='nearest')

plt.plot(x, y, 'o')
plt.plot(x2,f_1(x2),'-')
plt.legend(['wezly', 'najblizszy'], loc='best')
plt.show()

#sys.exit(0)


f_2 = interp1d(x, y, kind='previous')
f_3 = interp1d(x, y, kind='next')

plt.plot(x, y, 'o')

plt.plot(x2,f_1(x2),'-',x2,f_2(x2),'--',x2,f_3(x2),':')
plt.legend(['wezly', 'najblizszy', 'poprzedni', 'nastepny'], loc='best')
plt.show()

#sys.exit(0)


# FUNKCJE SKLEJANE - SPLINE

f_1 = interp1d(x, y, kind='slinear')

plt.plot(x, y, 'o', x2, np.sin(x2))
plt.plot(x2,f_1(x2),'-')
plt.legend(['wezly', 'sin(x)', 'liniowy'], loc='best')
plt.show()

#sys.exit(0)


f_2 = interp1d(x, y, kind='quadratic')
f_3 = interp1d(x, y, kind='cubic')


# Dodajemy Piecewise Cubic Hermite Interpolating Polynomial 
f_4 = pchip_interpolate(x,y,x2)

plt.plot(x, y, 'o', x2,np.sin(x2))

plt.plot(x2,f_1(x2),'-',x2,f_2(x2),'--',x2,f_3(x2),':',x2,f_4,'-')
plt.legend(['wezly', 'sin(x)', 'liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()


plt.plot(x, y, 'o', x2,np.sin(x2))

plt.plot(x2,f_3(x2),':',x2,f_4,'-')
plt.legend(['wezly', 'sin(x)', 'naturalny', 'Hermite'], loc='best')
plt.show()

#sys.exit(0)


# BŁĄD BEZWZGLĘDNY METOD SPLINE

err_1 = abs(f_1(x2) - np.sin(x2))
err_2 = abs(f_2(x2) - np.sin(x2))
err_3 = abs(f_3(x2) - np.sin(x2))
err_4 = abs(pchip_interpolate(x,y,x2) - np.sin(x2))

plt.plot(x2,err_1,'-',x2,err_2,'--',x2,err_3,':',x2,err_4,'-')
plt.legend(['liniowy', 'kwadratowy', 'cubic', 'pchip'], loc='best')
plt.show()


#sys.exit(0)


# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie koło maksimum

x2 = np.linspace(0, 1, 500)
x2 = x2*np.pi

f_4 = pchip_interpolate(x,y,x2)

plt.plot(x[1:4], y[1:4], 'o', x2,np.sin(x2),':')
 
plt.plot(x2,f_3(x2),'-.',x2,f_4,'-')
#plt.legend(['wezly', 'sin(x)', 'cubic', 'pchip'], loc='best')
plt.legend(['wezly', 'sin(x)', 'naturalny', 'Hermite'], loc='best')
plt.show()



# TYLKO WIELOMIANY 3-CIEGO STOPNIA - zachowanie dla funkcji płaskiej

x = np.linspace(-3, 3, 7)
y = [-1, -1, -1, 0, 1, 1, 1]

x2 = np.linspace(-3, 3, 1000)
                 
f_3 = interp1d(x, y, kind='cubic')
f_4 = pchip_interpolate(x,y,x2)

plt.plot(x,y,'o',x2,f_3(x2),'-',x2,f_4,'-.')
#plt.legend(['wezly','cubic','pchip'], loc='best')
plt.legend(['wezly','naturalny','Hermite'], loc='best')
plt.show()

# wielomiany bazowe Hermite'a

x = np.linspace(0,1,100)
y00 = 2*pow(x,3)-3*pow(x,2)+1
y10 = pow(x,3)-2*pow(x,2)+x
y01 = -2*pow(x,3)+3*pow(x,2)
y11 = pow(x,3)-pow(x,2)

plt.plot(x,y00,'-',x,y10,'--',x,y01,'-.',x,y11,':')
plt.legend(['h00','h10','h01','h11'], loc='best')
plt.show()
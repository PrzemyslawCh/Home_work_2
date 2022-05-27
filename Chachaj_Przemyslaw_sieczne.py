import math

def f(x):
    return math.sin(x*x-x+1/3.0)+0.5*x

def Chachaj_Przemyslaw_sieczne(x1, x2, eps):
    xkm = x1
    xk = x2
    xkp = xk - (x1 - xkm / f(xk) - f(xkm))

    while(abs(xkp - xk) > eps):
        xkm = xk
        xk = xkp
        xkp = xk - (f(xk) * (xk - xkm) / (f(xk) - f(xkm)))
        
    x = xkp  
    return x
    
print(Chachaj_Przemyslaw_sieczne(-1.1, -1.0, 0.0000000000000001))
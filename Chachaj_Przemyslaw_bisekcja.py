import math

def func(x):
    return (x-1)*(x-5)*(x-3)

def Chachaj_Przemyslaw_bisekcja(a,b,eps):  
    if(func(a)*func(b) > 0):
       return ":("
    while(b - a > eps):   
        c = round((a + b) / 2, 3)
        if(func(c) == 0):
            return c
        if(func(a)*func(b) < 0):
            b = c    
        else:                     
            a = c        

print(Chachaj_Przemyslaw_bisekcja(6, 7, 0.0001))    
print(Chachaj_Przemyslaw_bisekcja(2, 4, 0.1))   

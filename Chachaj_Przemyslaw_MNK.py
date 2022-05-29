import math

import numpy as np

x = np.array([-1, 0, 1, 2])
y = np.array([4, -1, 0, 7])
n = 2

sumX = np.sum(x)
sumY = np.sum(y)
sumXY = np.sum(x*y)

def Chachaj_Przemyslaw_gauss_jordan(M, b):
    n = len(M)
    x = [0, 0]
    for i in range(0, n - 1):
        for j in range(i + 1,n):
            m = M[j][i] / M[i][i]     
            b[j] -= b[i] * m  
            for k in range(i, n ):
                M[j][k] -=  M[i][k]*m
                               
    x[n -1] = b[n -1] / M[n-1][n-1]
    for g in range(n -2, -1, -1):
        suma = b[g]
        for h in range(g+1, n):
            suma -= M[g][h] * x[h]
        x[g] = suma/ M[g][g]       
    
    return M, x


def Chachaj_Przemyslaw_MNK(x, y, n):
    A = np.zeros((n + 1, n + 1))
    B = np.zeros((n + 1, 1))
    print(A)
    print(B)
    A[0][0] = 2 * n
    for g in range(1, n + 1):
        A[0][g] = np.sum(x**g)
        print(A)
    for h in range(1, n + 1):  
        for r in range(0, n + 1):
            A[h][r] = (A[h-1][r] * np.sum(x**(r+1)))/A[h-1][r]
    print(A)
    
    B[0][0] = np.sum(y)
    for j in range(1, n + 1):
        B[j][0] = B[0][0]*np.sum(x)
                
    return Chachaj_Przemyslaw_gauss_jordan(A, B)

    
print(Chachaj_Przemyslaw_MNK(x, y, n))


    

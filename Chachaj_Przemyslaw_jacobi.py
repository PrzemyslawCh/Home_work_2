import math
from numpy import linalg

def norm(x1, x0):
  Euclid_norm = 0

  for i in range(len(x1)):
    Euclid_norm += (x1[i] - x0[i])**2

  Euclid_norm = sqrt(Euclid_norm)

  return Euclid_norm

def Chachaj_Przemyslaw_jacobi(A,b,eps):
  n = len(b)
  k = 0
  x = [0.0 for i in range(n)]
  x0 = [0.0 for i in range(n)]

  IsDominate = True

  for i in range(n):
    sum = 0

    for j in range(n):
      if i != j:
        sum += abs(A[i][j])

    if abs(A[i][i]) < sum:
      IsDominate = False

  if (IsDominate == False):
    return

  for k in range(2):

    for i in range(n):
      sum = 0

      for j in range(n):
        if i != j:
          sum += A[i][j] * x0[j]

      x[i] = (b[i] - sum) / A[i][i]

    for i in range(len(x)):
      x0[i] = x[i]

  return x

A = [[4,-1,-1,0],
    [-1,4,0,-1],
    [-1,0,4,-1],
    [0,-1,-1,4]]

b = [1,2,0,1]

print(Chachaj_Przemyslaw_jacobi(A, b, 1))

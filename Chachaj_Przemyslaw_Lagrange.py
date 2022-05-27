from unittest import result
import numpy
import matplotlib.pyplot as plt

xw = [-2, 1, 4]
yw = [5, 3, 7]
x = [3,4,6,7]
n = 3

def Chachaj_Przemyslaw_Lagrange(x, xw, yw, n):

  result = [0 for k in range(len(x))]

  for i in range(n):
    numerator = [1 for k in range(len(x))]
    denominator = [1 for k in range(len(x))]

    for j in range(n):
      if j != i:
        for k in range(len(x)):
          numerator[k] *= x[k] - xw[j]
          denominator[k] *= xw[i] - xw[j]

    for j in range(len(x)):
      result[j] += yw[i] * (numerator[j] / denominator[j])

  return result


def Efekt_Runge(k):
  x = numpy.linspace(-1, 1, num=101)
  y = abs(x)
  plt.plot(x, y, '-')

  for i in range(k):
    X = numpy.linspace(-1,1,2*i+1)
    Y = [0 for k in range(len(X))]

    for j in range(len(X)):
      Y[j] = abs(X[j])

    Z = Chachaj_Przemyslaw_Lagrange(x, X, Y, len(X))
    plt.plot(x, Z)

  plt.show()
    
print(Chachaj_Przemyslaw_Lagrange(x, xw, yw, n))
print(Efekt_Runge(5))

import numpy as np

a = np.array([1,2,3])
b = a
b[0] = 42
print (b)
print (a)


x = np.array([1,2,3])
y = x.copy()
y[0] = 36
print (y)
print (x)
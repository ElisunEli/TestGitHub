import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a)

print(a.shape)

b = np.arange(10)

print(b)

b = np.arange(10, 100, 10)
print(b)
print(b.shape)

b = np.zeros(10)

print(b)

b = np.zeros(10, dtype=int)

print(b)

b = np.zeros(10, dtype=str)

print(b)

b = np.ones(5)

print(b)


a = a.reshape(2, 5)
print(a)

a = a.reshape(1, 10)
print(a)

d = np.ones(10, dtype=int)
e = np.ones(10, dtype=int)
f = d + e
print(d, e, f)

print(a%2 == 0)

a[a<5] = 10
print(a)


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

g = a[2:5]

print(g)

a[3] = 1000

print(g)


a = np.ones(100, dtype=int).reshape(10, 10)
print(a)
a[2][3] = 100
print(a)
a[8] = 7
print(a)

a[:, 5] = 4
a[0:2, 0:2] = 3
a[ a == 1] = 55
print(a)
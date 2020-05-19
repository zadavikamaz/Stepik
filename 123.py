import numpy as np

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
# a = 10
# b = 10
V1 = np.array(a)
V2 = np.array(b)
V3 = V1 + V2
V4 = V1[0::2]*V2[::-1][0::2]

print(V1)
print(V2)
print(V3)
print(V1[1::2], V2[::-1][0::2])
print(V4)
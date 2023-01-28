import numpy as np

# l = [1,2,3]
# a = np.array([1,2,3])

# l.append(4)
# print (l)
# a.append(4)
# print (a)


# l = l + [4]
# print (l)
# a = a + np.array([4])
# print (a)


# l = l * 2
# print (l)
# a = a * 2
# print (a)


# a = np.sqrt(a)
# print (a)

# a = np.log(a)
# print (a)


l1 = [1,2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print (dot)

dot = np.dot(a1, a2)
print (dot)

sum1 = a1 * a2
dot = np.sum(sum1)
print (dot)

dot = a1 @ a2
print (dot)

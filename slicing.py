import numpy as np

# a = np.array([[1,2,3,4],[5,6,7,8]])
# print (a)

# b = a[0,1:3]
# # b = a[1,1:3]
# print (b)

# a = np.array([[1,2],[3,4],[5,6]])
# print (a)
# # [[1 2]
# #  [3 4]
# #  [5 6]]

# bool_idx = a > 2
# print (bool_idx)
# # [[False False]
# #  [ True  True]
# #  [ True  True]]

# print (a[bool_idx])
# # [3 4 5 6]

# print (a[a > 2])
# # [3 4 5 6]

# b = np.where(a>2, a, -1)
# print (b)


a = np.array([10,19,30,41,50,61])
print(a)
# b = [1,3,5]
# print(a[b])

even = np.argwhere(a%2==0).flatten()

print(a[even])

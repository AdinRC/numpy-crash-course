import numpy as np

# a = np.array([[1,2],[3,4]])
# print (a)
# b = np.array([[5,6]])
# # c = np.concatenate((a,b), axis=None)
# c = np.concatenate((a,b.T), axis=1)
# print (c)


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
# hstack
# c = np.hstack((a,b))
# print(c)

c = np.vstack((a,b))
print(c)

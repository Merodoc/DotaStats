"""
#ass3PCA.py
"""

import numpy as np

""" Load in data """
X = np.genfromtxt('irisX.csv',delimiter = ',')
n = X.shape[0]

""" Subtract column mean from every column """
X = X - X.mean(axis=0)
""" G is x transpose """
G = X.T @ X
""" Decompose Sigma to get U and D^2 """
U, D , vh =np.linalg.svd(G/n)
#projected points
Y = X @ np.outer(U[:,0], U[:,0])


print("D^2 = "+ str(D))
print("U_1 = "+str(U))

""" v is the sum of d_l,l^2 or sum of elements in D """
v = sum(D)

print(v)

""" Divide first principal component by v """

sigma2 = D[0]/v

print(sigma2)


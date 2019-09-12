# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:42:22 2019

@author: Rowan
"""

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
# generate data
np.random.seed(12345)
N = 100
X = np.random.randn(N)
q = scipy.stats.norm.ppf(0.95)
y = np.zeros(N)
y[X>=q] = 1
y[X<= -q] = 1
X = X.reshape(-1,1)

def euclidDistance(y,x):
    """Provides the euclidean distance between y and x"""
    d = np.sqrt((y - x)**2)
    return d

def KNN(train, test, k):
    """ adds k nearest neighbors to test in euclidean distance to list KNN """
    xord = []
    for i in range(len(train)):
        xord.append((euclidDistance(test,train[i]), i))
    xord.sort()
    KNN = xord[0:k]
    return KNN


def KNNClass(train_input, train_output, test_input, k):
    """ Classifies test_input to a class based on k-nearest neighbors class """
    knn = KNN(train_input, test_input, k)
    votes  = []
    for k, v in knn:
        votes.append(train_output[v])
    
    response = scipy.stats.mode(votes)
    return(response)

test1 = KNNClass(X,y,1,5)
test2 = KNNClass(X,y,1.96,5)
print(test1)
print(test2)

def h(x):
    """ define h(x) as known """
    h = 1/(1+np.exp(-x))
    return(h)

def mu(x,beta):
    """" define mu as known """
    mu = h(np.transpose(x)*beta)
    return mu
    
def grad(x, beta, y):
    """ returns the gradient of tau """
    grad = (1/len(x))*np.sum(np.multiply((mu(x,beta)-y),x))
    return(grad)
    
def Hessian(beta, x):
    """" Returns the Hessian of x """
    Mu = mu(x,beta)
    Hessian = (1/len(x))*np.sum(np.multiply(np.multiply(Mu,np.subtract(1,Mu)),np.multiply(x,np.transpose(x))))
    return(Hessian)
    
def betahat(beta,x,y,n):
    """ estimates betahat with newtons method """
    while n > 0:
        beta =  beta - (1/(Hessian(beta, x)))*grad(x,beta,y)
        n -= 1
    return(beta)
    
newX = []
for i in range(len(X)):
    newX.append(X[i][0])


def LogisticClassifier(beta,x,y,n,test):
    """ compares the test x and beta estimate to the boundary """
    bestimate = betahat(beta,x,y,n)
    if np.transpose(test)*bestimate >= 0:
        print("x is in class 1")
    else:
        print("x is in class 0")
        

LogisticClassifier(0,newX,y,10**6,1)
LogisticClassifier(0,newX,y,10**6,1.96)


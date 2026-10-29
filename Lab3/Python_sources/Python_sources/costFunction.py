import numpy as np
from sigmoid import *


def cost_function(theta, X, y):
    m = y.size

    # You need to return the following values correctly
    cost = 0
    grad = np.zeros(theta.shape)

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta
    #                You should set cost and grad correctly.
    #

    # ===========================================================

    cost = (-1 / m) * (
        np.dot(y, np.log(sigmoid(np.dot(X, theta))))
        + np.dot((1 - y), np.log(1 - sigmoid(np.dot(X, theta))))
    )
    grad = (1 / m) * np.dot(X.T, (sigmoid(np.dot(X, theta)) - y))

    return cost, grad

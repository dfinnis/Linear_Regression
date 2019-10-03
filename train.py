import numpy as np
from predict import predict

def predict(X, theta):
    return theta[0] + (theta[1] * X)

def cost(X, y, theta):
    m = len(X)
    hypothesis = predict(X, theta)
    J = 1 / (2 * m) * np.sum(np.square(hypothesis - y))
    return (J)

def fit_with_cost(X, y, theta, alpha, num_iters):
    m = len(X)
    J_history = []
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
        J_history.append(cost(X, y, theta))
    return theta, J_history
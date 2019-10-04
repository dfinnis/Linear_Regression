import numpy as np
import pandas as pd
import matplotlib as plt
import statistics as stat
from train import fit_with_cost

data = pd.read_csv("data.csv")

X = np.array(data['km'], dtype='float64')
y = np.array(data['price'], dtype='float64')

def feature_normalize(X):
    mu = stat.mean(X)
    sigma = stat.stdev(X)
    normalized_features = (X-mu)/sigma if sigma != 0 else X
    return normalized_features

X_norm = feature_normalize(X)

def predict(X, theta):
    return theta[0] + (theta[1] * X)

import matplotlib.pyplot as plt

def visualize(theta):
    fig = plt.figure()
    ax = plt.axes()

    plt.scatter(X, y, color='blue')

    x_max = np.max(X) + 10000
    x_min = np.min(X) - 10000
    ax.set_xlim([x_min, x_max])
    ax.set_ylim(np.min(y) - 1000, np.max(y) + 1000)
    ax.scatter(X, y, color='blue')
    
    reg_line = theta[0] + X_norm * theta[1]
    ax.plot(X, reg_line, 'r-', X, y, 'o')

    plt.title("Price over Distance Driven")
    plt.xlabel("kilometers")
    plt.ylabel("price")
    plt.show()

# def cost(X, y, theta):
#     m = len(X)
#     hypothesis = predict(X, theta)
#     J = 1 / (2 * m) * np.sum(np.square(hypothesis - y))
#     return (J)

# def fit_with_cost(X, y, theta, alpha, num_iters):
#     m = len(X)
#     J_history = []
#     for i in range(num_iters):
#         hypothesis = predict(X, theta)
#         theta[0] -= alpha / m * np.sum(hypothesis - y)c
#         theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
#         J_history.append(cost(X, y, theta))   
#     return theta, J_history

theta = np.array([0, 0], dtype='float64')

theta, J_history = fit_with_cost(X_norm, y, theta, 0.01, 1500)

fit = plt.figure()
ax = plt.axes()
ax.plot(J_history)
    
visualize(theta)
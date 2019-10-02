import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv("data.csv")

data.plot.scatter('km', 'price')

X = np.array(data['km'], dtype='float64')
y = np.array(data['price'], dtype='float64')

theta = np.array([0, 0], dtype='float64')

def predict(X, theta):
    return (theta[0] + (theta[1] * X))

def fit(X, y, theta, alpha, num_iters):
    m = len(X)
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
    return theta

theta = fit(X, y, theta, 0.01, 1500)
print(theta)

import matplotlib.pyplot as plt

def visualize(theta):
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlim([22000,25000])
    ax.set_ylim(3000, 9000)
    ax.scatter(X, y)
    line_x = np.linspace(12000,250000, 1000)
    line_y = theta[0] + line_x * theta[1]
    ax.plot(line_x, line_y)
    plt.show()

visualize(theta)

def cost(X, y, theta):
    m = len(X)
    hypothesis = predict(X, theta)
    J = 1 / (2 * m) * np.sum(np.square(hypothesis - y))
    return (J)

cost(X, y, [0, 0])

cost(X, y, [-1, 2])

def fit_with_cost(X, y, theta, alpha, num_iters):
    m = len(X)
    J_history = []
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
        J_history.append(cost(X, y, theta))   
    return theta, J_history

theta = np.zeros(2)

theta, J_history = fit_with_cost(X, y, theta, 0.01, 1500)

fit = plt.figure()
ax = plt.axes()
ax.plot(J_history)
    
visualize(theta)
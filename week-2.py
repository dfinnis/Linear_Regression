import numpy as np
import pandas as pd
import matplotlib as plt
import statistics as stat

# with warnings.catch_warnings():
#     warnings.filterwarnings('ignore', r'All-NaN (slice|axis) encountered')

data = pd.read_csv("data.csv")

# data.plot.scatter('km', 'price')

X = np.array(data['km'], dtype='float64')
y = np.array(data['price'], dtype='float64')

def feature_normalize(X):
    mu = stat.mean(X)
    sigma = stat.stdev(X)
    normalized_features = (X-mu)/sigma if sigma != 0 else X
    return normalized_features

X_norm = feature_normalize(X)

theta = np.array([0, 0], dtype='float64')

def predict(X, theta):
    return theta[0] + (theta[1] * X)

def fit(X, y, theta, alpha, num_iters):
    m = len(X)
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
        # loss = predict(X, theta) - y
        # tmp_theta0 = theta[0] - (alpha / m) * sum(loss)
        # tmp_theta1 = theta[1] - (alpha / m) * sum(loss * X.T)
        # theta = [tmp_theta0, tmp_theta1]
    return theta

theta = fit(X_norm, y, theta, 0.01, 1500)
print(theta)

import matplotlib.pyplot as plt

def visualize(theta):
    fig = plt.figure()
    ax = plt.axes()
    # ax = fig.add_subplot(111)
    
    # ax.scatter(X, y, color='blue')

    x_max = np.max(X) + 10000
    x_min = np.min(X) - 10000
    ax.set_xlim([x_max, x_min])
    ax.set_ylim(np.max(y) + 1000, np.min(y) - 1000)
    ax.scatter(X, y, color='blue')
    
    xplot = np.linspace(x_max, x_min, 100)
    yplot = theta[0] + xplot * theta[1]
    ax.plot(xplot, yplot, color='red')

    plt.title("Price over Distance Driven")
    plt.xlabel("kilometers")
    plt.ylabel("price")
    plt.show()

    #####

    # line_x = np.linspace(12000, 250000, 1000)
    # line_y = theta[0] + line_x * theta[1]
    # plt.plot(line_x, line_y, color='red')

    # fig = plt.figure()
    # ax = plt.axes()
    # ax.set_xlim([22000,25000])
    # ax.set_ylim(3000, 9000)
    # ax.scatter(X, y)
    # line_x = np.linspace(12000,250000, 1000)
    # line_y = theta[0] + line_x * theta[1]
    # ax.plot(line_x, line_y)
    # plt.show()

visualize(theta)

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

theta = np.zeros(2)
# X_norm = feature_normalize(X)

theta, J_history = fit_with_cost(X_norm, y, theta, 0.01, 1500)

fit = plt.figure()
ax = plt.axes()
ax.plot(J_history)
    
visualize(theta)
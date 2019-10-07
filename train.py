import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plot
import tools as tools
import visualize as v

def feature_normalize(X):
    mu = np.mean(X)
    sigma = np.std(X)
    normalized_features = (X-mu)/sigma if sigma != 0 else X
    return normalized_features, mu, sigma

def predict(X, theta):
    return theta[0] + (theta[1] * X)

def cost(X, y, theta):
    m = len(X)
    hypothesis = predict(X, theta)
    J = 1 / (2 * m) * np.sum(np.square(hypothesis - y))
    return (J)

def fit(X, y, theta, alpha, num_iters):
    m = len(X)
    J_history = []
    weight_list = []
    for i in range(num_iters):
        hypothesis = predict(X, theta)
        theta[0] -= alpha / m * np.sum(hypothesis - y)
        theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X)) 
        J_history.append(cost(X, y, theta))   
        weight_list.append([theta[0], theta[1]]) 
    return theta, J_history, weight_list 

def main():
    alpha, num_iterations, animate = tools.parse_args()

    data = pd.read_csv("data.csv")
    X = np.array(data['km'], dtype='float64')
    y = np.array(data['price'], dtype='float64')
    X_norm, mu, sigma = feature_normalize(X)

    theta = np.array([0, 0], dtype='float64')
    theta, J_history, weight_list = fit(X_norm, y, theta, alpha, num_iterations)
    
    v.visualize_cost(J_history)
    if animate == True:
        v.visualize_animate(weight_list, X_norm, X, y, num_iterations)
    else:
        v.visualize_regression(theta, X_norm, X, y)

    tools.save_theta(theta, mu, sigma)

if __name__ == '__main__':
    main()
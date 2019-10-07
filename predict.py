import sys
import numpy as np
from train import feature_normalize

# def denormalize(price, mu, sigma):
#     price_2 = price * float(sigma) + float(mu)
#     print(price_2)
#     # price = (price + mu) * sigma
#     return price_2

def predict(km, theta, mu, sigma):
    # km, mu, sigma = feature_normalize(km)
    price = theta[0] + theta[1] * km
    # price = denormalize(price, mu, sigma)
    return price

def find_theta():
    theta = np.array([0, 0], dtype='float64')
    mu = 0
    sigma = 0
    try:
        t = open('Theta', 'r')
        line = t.readlines()
        index = line[0].index('=')
        theta[0] = line[0][index+1:]
        theta[1] = line[1][index+1:]
        index = line[2].index('=')
        mu = line[2][index+1:]
        index = line[3].index('=')
        sigma = line[3][index+1:]
        # print(theta[0])
        # print(theta[1])
        # print(mu)
        # print(sigma)
    except Exception:
        print("Using default theta values (0,0)")
    return theta, mu, sigma

def main():
    km = input('Please enter mileage: ')
    if (km.isnumeric()) == False:
        print('The milage specified is invalid')
        exit()
    km = int(km)
    theta, mu, sigma = find_theta()
    price = predict(km, theta, mu, sigma)
    print("The price of a car at {}km is estimated at {}" .format(km, price))

if __name__ == '__main__':
    main()





# def fit(X, y, theta, alpha, num_iters):
    # m = len(X)
    # for i in range(num_iters):
        # hypothesis = predict(X, theta)
        # theta[0] -= alpha / m * np.sum(hypothesis - y)
        # theta[1] -= alpha / m * np.dot((hypothesis - y), np.transpose(X))
    # return theta
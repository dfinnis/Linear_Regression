import sys
import numpy as np
from train import feature_normalize

def predict(km, theta, mu, sigma):
    if not mu == 0 and not sigma == 0:
        km = (km - mu) / sigma
    price = theta[0] + theta[1] * km
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
        mu = (line[2][index+1:])
        index = line[3].index('=')
        sigma = (line[3][index+1:])
        mu = float(mu)
        sigma = float(sigma)
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

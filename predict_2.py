import sys
import numpy as np
# from train_2 import train_2

def predict(km, theta):
    price = theta[0] + theta[1] * float(km)
    return price

def find_theta():
    theta = np.array([0, 0], dtype='float64') 
    try:
        t = open('Theta', 'r')
        line = t.readlines()
        index = line[0].index('=')
        theta[0] = line[0][index+1:]
        theta[1] = line[1][index+1:]
    except Exception:
        print("Using default theta values (0,0)")
    return theta

def main():
    km = input('Please enter mileage: ')
    if (km.isnumeric()) == False:
        print('The milage specified is invalid')
        exit()
    km = int(km)
    theta = find_theta()
    price = predict(km, theta)
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
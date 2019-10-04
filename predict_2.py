import sys
import numpy as np
# from train_2 import train_2

def predict(km):
    theta = np.array([0, 0], dtype='float64')
    price = theta[0] + theta[1] * float(km)
    return price

def main():
    km = input('Please enter mileage: ')
    if (km.isnumeric()) == False:
        print('The milage specified is invalid')
        sys.exit()
    km = int(km)
    print(km) ########
    price = predict(km)
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
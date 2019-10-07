from train import feature_normalize
import tools as tools

def predict(km, theta, mu, sigma):
    if not mu == 0 and not sigma == 0:
        km = (km - mu) / sigma
    price = theta[0] + theta[1] * km
    return price

def main():
    km = input('Please enter mileage: ')
    if (km.isnumeric()) == False:
        print('The milage specified is invalid')
        exit()
    km = int(km)
    theta, mu, sigma = tools.find_theta()
    price = round(predict(km, theta, mu, sigma), 2)
    if price < 0:
        print("The price of a car at {}km is estimated at {}. Junk it!" .format(km, price))
    else:
        print("The price of a car at {}km is estimated at {}" .format(km, price))

if __name__ == '__main__':
    main()

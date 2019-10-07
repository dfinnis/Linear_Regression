import numpy as np
import pandas as pd
import argparse

def parse_args():
    my_parser = argparse.ArgumentParser(description='List the content of a folder')
    my_parser.add_argument('-a',
                        '--alpha',
                        type=float,
                        help='set learning rate (alpha). Default 0.01')
    my_parser.add_argument('-n',
                        '--num_iterations',
                        type=int,
                        help='set number of iterations. Default 1500')
    my_parser.add_argument('-v',
                        '--animate',
                        action='store_true',
                        help='Animate visualizer. Default unanimated')
    args = my_parser.parse_args()

    alpha = args.alpha
    num_iterations = args.num_iterations
    animate = args.animate
    if alpha is None:
        alpha = 0.01
    if num_iterations is None:
        num_iterations = 1500
    return alpha, num_iterations, animate

def save_theta(theta, mu, sigma):
    if theta[0] == 0.0 and theta[1] == 0.0:
        print("Saving theta aborted as theta is zero")
    else:
        try:
            theta_file = open('Theta', 'w')            
            theta_file.write('theta[0] = {}\ntheta[1] = {}\nmu = {}\nsigma = {}' .format(theta[0], theta[1], mu, sigma))
            theta_file.close
        except Exception:
            print("Saving theta failed")

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

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainer.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aschukin <aschukin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/31 14:20:25 by aschukin          #+#    #+#              #
#    Updated: 2018/11/12 22:01:29 by aschukin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#plot
#find cost
#gradient descent
#print results
#plot, cost, gradient descent, visualize J, print results
# split X and Y into separate numpy arrays called x and y


from sys import argv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # for plotting the data

if argv[1] :
    file = argv[1]

data = pd.read_csv(file, sep=',', names=["X","Y"], skiprows=1, dtype=int)
data['ones'] = 1
x = data[['ones', 'X']].values
y = data['Y'].values
m = len(data)

theta = np.array([0, 0])

# Gradient Descent
#iterations = 1500
alpha = 0.01

# Compute Cost
for i in range(1500):
    theta -= 1/(2*m) * np.dot((np.transpose(x * theta) - y)), ((np.dot(X, theta)) - y)

print(theta)
print(J)

plt.plot(x, y, 'r+')
plt.title("Price over Distance Driven")
plt.xlabel("kilometers")
plt.ylabel("price")
plt.show()
#print(x)




#x.resize((1, 24))
#a = np.ones([1, m], dtype=int)
#x = np.column_stack((a, x))


#x = x.shape(x, (-1, 2))
#np.insert(x, [1], [1], axis=1)
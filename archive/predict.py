# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aschukin <aschukin@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/01 14:01:10 by aschukin          #+#    #+#              #
#    Updated: 2018/11/01 14:01:14 by aschukin         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

plot, cost, gradient descent, visualize J, print results

 J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
 parameter for linear regression to fit the data points in X and y

# Compute Cost
J = 1/(2*m) * ((X * theta) - y)' * ((X * theta) - y)


import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plot
import matplotlib.animation as animation

def visualize_cost(J_history):
    plot.figure()
    ax = plot.axes()
    plot.title("Error rate")
    plot.xlabel("Number of Iterations")
    plot.ylabel("Mean Squared Error")
    ax.plot(J_history)

def visualize_regression(theta, X_norm, X, y):
    fig = plot.figure()
    ax = plot.axes()
    
    plot.scatter(X, y, color='blue')

    x_max = np.max(X) + 10000
    x_min = np.min(X) - 10000
    ax.set_xlim([0, x_max])
    ax.set_ylim(np.min(y) - 1000, np.max(y) + 1000)
    ax.scatter(X, y, color='blue')
    
    reg_line = theta[0] + X_norm * theta[1]
    ax.plot(X, reg_line, 'r-', X, y, 'o')

    plot.title("Price over Distance Driven")
    plot.xlabel("kilometers")
    plot.ylabel("price")
    plot.show()

def visualize_animate(weight_list, X_norm, X, y, num_iterations):
    fig, ax = plot.subplots()
    ax.scatter(X, y)
    line1, = ax.plot([], [], 'r-')
    line2, = ax.plot([], [], 'o')

    x_max = np.max(X) + 10000
    x_min = np.min(X) - 10000
    ax.set_xlim([0, x_max])
    ax.set_ylim(np.min(y) - 1000, np.max(y) + 1000)
    weight_list = np.array(weight_list)

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return [line1, line2]

    def animate(i):
        theta_0, theta_1 = weight_list[i,]
        reg_line = theta_0 + X_norm * theta_1
        line1.set_data(X, reg_line)
        line2.set_data(X, y)
        return [line1, line2]

    plot.title("Price over Distance Driven")
    plot.xlabel("kilometers")
    plot.ylabel("price")
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_iterations, interval=5, blit=True)
    plot.show()
    plot.ioff()
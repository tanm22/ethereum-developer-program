from random import random
from matplotlib import pyplot as plt
import numpy as np
import math


class Bertrand:


    # Initializing the program
    def __init__(self):
        # creates a figure and an axses object(the plotting area)
        self.fig, self.axs = plt.subplots(3, figsize=(10,30), sharex=True)
        # side of the equilateral triangle
        self.a = 0
        # Radius of the circle
        self.r = 1
        # Number of iterations
        self.n = 500

        # Setting up the plots
        plt.setp(self.axs, xlim=(-self.r-1,self.r+1), ylim=(-self.r-1,self.r+1))


    # Calculates distance between two points
    def distance(self, A, B):
        return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)


    # Draws a circle on the subplots
    def draw_circle(self, r, axs):

        circle = plt.Circle((0, 0), r, color='black', fill=False)
        # Artist: represent a standard graphical object, knows how to use the renderer to paint it
        axs.add_artist(circle)


    # Draws a triangle on the subplots
    def draw_triangle(self, P, axs):
        x, y = P
        # stack arrays in sequence horizontally (column wise)
        points = np.hstack([x, y])
        axs.plot(x, y, color='cyan', marker='o')

        # calculate the other 2 points of the equilateral triangle
        # rotate P by 120, 240 degrees => A, B points
        angle = np.deg2rad(120)
        x = (P[0] * np.cos(angle)) - (P[1] * np.sin(angle))
        y = (P[0] * np.sin(angle)) + (P[1] * np.cos(angle))
        A = (x, y)
        points = np.vstack([points, [x, y]])
        axs.plot(x, y, color='cyan', marker='o')

        angle = np.deg2rad(240)
        x = P[0] * np.cos(angle) - (P[1] * np.sin(angle))
        y = P[0] * np.sin(angle) + (P[1] * np.cos(angle))
        B = (x, y)

        self.a = self.distance(A, B)
        points = np.vstack([points, [x, y]])
        axs.plot(x, y, color='cyan', marker='o')

        points = np.vstack([points, [P[0], P[1]]])
        axs.plot(points[:, 0], points[:, 1], linewidth=3, color='blue', label='Equilateral Triangle')

    def first_method(self):

        self.axs[0].set_title('Bertrand paradox, 1st method')
        self.draw_circle(self.r, self.axs[0])

        # get a fixed P point on the circumference
        alpha = random() * (2 * np.pi)
        x, y = self.r * np.cos(alpha), self.r * np.sin(alpha)
        P = (x, y)
        self.draw_triangle(P, self.axs[0])

        favorable = 0
        # generate random points on the circumference
        for i in range(self.n):
            alpha = random() * (2 * np.pi)
            x, y = self.r * np.cos(alpha), self.r * np.sin(alpha)
            # the new point
            M = (x, y)
            self.axs[0].plot(x, y, color='black', marker='.')
            if self.distance(P, M) > self.a:
                self.axs[0].plot([P[0], x], [P[1], y], color='green')
                favorable += 1
            else:
                self.axs[0].plot([P[0], x], [P[1], y], color='red')

        print('Method 1: {0}/{1} = {2}'.format(favorable, self.n, favorable/self.n))

        self.axs[0].legend()
        self.axs[0].grid()

    def second_method(self):
        self.axs[1].set_title('Bertrand paradox, 2nd method')
        self.draw_circle(self.r, self.axs[1])

        # draw a random radius
        alpha = random() * (2 * np.pi)
        x, y = self.r * np.cos(alpha), self.r * np.sin(alpha)
        self.axs[1].plot([0, x], [0, y], color='black', linewidth=3, label='radius')

        # perpendicular angle to alpha
        beta = alpha + np.pi/2
        x, y = self.r * np.cos(alpha), self.r * np.sin(alpha)
        # get a fixed P point on the circumference
        P = (x, y)
        self.draw_triangle(P, self.axs[1])

        A = r_middlex, r_middley = self.r / 2 * np.cos(alpha), self.r / 2 * np.sin(alpha)
        self.axs[1].plot(r_middlex, r_middley, color='darkblue', marker='o', label='middle of the radius')

        favorable = 0
        for i in range(self.n):
            # random point on the radius
            m = random() * self.r
            x, y = m * np.cos(alpha), m * np.sin(alpha)
            M = (x, y)
            self.axs[1].plot(x, y, color='orange', marker='.')

            # perpendicular line to the radius in the generated point
            x, y = M
            # cord length
            length = math.sqrt(pow(self.r, 2) - pow(self.distance(M, (0, 0)), 2))
            x1, y1 = x + length * np.cos(beta), y + length * np.sin(beta)
            x2, y2 = x - length * np.cos(beta), y - length * np.sin(beta)
            if self.distance(A, (0, 0)) < self.distance(M, (0, 0)):
                self.axs[1].plot([x1, x2], [y1, y2], color='red')
            else:
                self.axs[1].plot([x1, x2], [y1, y2], color='green')
                favorable += 1

        print('Method 2: {0}/{1} = {2}'.format(favorable, self.n, favorable / self.n))

        self.axs[1].legend()
        self.axs[1].grid()

    def third_method(self):
        self.axs[2].set_title('Bertrand paradox, 3rd method')
        self.draw_circle(self.r, self.axs[2])

        # get a fixed P point on the circumference
        alpha = random() * (2 * np.pi)
        P = x, y = self.r * np.cos(alpha), self.r * np.sin(alpha)
        self.draw_triangle(P, self.axs[2])

        # draw a smaller circle
        circle = plt.Circle((0, 0), self.r / 2, color='grey', fill=False)
        self.axs[2].add_artist(circle)

        favorable = 0
        for i in range(self.n):
            # generate a new point within the circle
            alpha = random() * (2 * np.pi)
            rand_r = math.sqrt(random())
            x, y = rand_r * self.r * np.cos(alpha), rand_r * self.r * np.sin(alpha)
            # the new point
            M = (x, y)
            if self.distance(M, (0, 0)) <= self.r / 2:
                self.axs[2].plot(x, y, color='green', marker='.')
                favorable += 1
            else:
                self.axs[2].plot(x, y, color='red', marker='.')

        print('Method 3: {0}/{1} = {2}'.format(favorable, self.n, favorable / self.n))

        self.axs[2].legend()
        self.axs[2].grid()


def main():
    bert = Bertrand()
    print("Green lines are those with side length greater than the side of the triangle and red lines are those that are not.\n\n")
    bert.first_method()
    bert.second_method()
    bert.third_method()
    plt.savefig("plots.png")


if __name__ == '__main__':
    main()
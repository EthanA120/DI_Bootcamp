# TASK: Circle
import math
import matplotlib.pyplot as plt


class Circles:
    """
        The goal is to create a class that represents a simple circle.
        A Circle can be defined by either specifying the radius or the diameter.
        The user can query the circle for either its radius or diameter.

        Other abilities of a Circle instance:

            Compute the circle’s area
            Print the circle and get something nice
            Be able to add two circles together
            Be able to compare two circles to see which is bigger
            Be able to compare two circles and see if there are equal
            Be able to put them in a list and sort them
    """

    def __init__(self, radius):
        self.radius = radius
        self.name = "R" + str(self.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def print_circle(self):
        circle_plot = plt.Circle((0, 0), self.radius, color="tab:blue", linewidth=3, fill=False)
        ax = plt.gca()
        ax.axis("equal")
        ax.grid(True)
        ax.set_xlim((-(self.radius + 1), self.radius + 1))
        ax.set_ylim((-(self.radius + 1), self.radius + 1))
        ax.add_patch(circle_plot)
        plt.show()

        print(f"The circle radius is {self.radius}")

    def add_circles(self, other_circle):
        return self.radius + other_circle.radius

    def compare(self, other_circle):
        if self.radius > other_circle.radius:
            print(f"{self.name} is bigger than {other_circle.radius}")
        elif self.radius < other_circle.radius:
            print(f"{self.name} is smaller than {other_circle.radius}")
        else:
            print(f"{self.name} is equal to {other_circle.radius}")

    def sort_circles(self, *args):
        sorted_circles = sorted([self] + [circle for circle in args], key=lambda a: a.radius)
        return [circle.name for circle in sorted_circles]


circle = Circles(2)
other_circle = Circles(3)
circle.print_circle()
print(circle.add_circles(other_circle))
circle.compare(other_circle)
print(circle.sort_circles(other_circle))

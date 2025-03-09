import matplotlib.pyplot as plt
import numpy as np

"""
Monte Carlo Simulation: Estimating the Area of a Right Triangle Inside a Unit Square

This simulation generates random points within a unit square (1x1) and calculates the proportion of points 
that fall inside a right triangle defined within the square. The estimated area of the triangle is determined 
by computing the ratio of points inside the triangle to the total generated points.

Steps:
1. Generate `num_points` random (x, y) coordinates within the unit square.
2. Check if the point falls inside the right triangle (x >= y condition).
3. Compute the estimated area as the ratio of points inside the triangle to total points.
4. Visualize the results with a scatter plot, highlighting points inside and outside the triangle.
"""

class Triangle:
    def __init__(self, num_points):
        
        self.num_points = num_points
        self.points_in_triangle = []
        self.area = 0

    def monte_carlo_triangle_area(self):
       
        np.random.seed(100)
        self.all_points = np.random.rand(self.num_points, 2)
        self.points_in_triangle = self.all_points[self.all_points[:, 0] >= self.all_points[:, 1]]
        self.area = len(self.points_in_triangle) / self.num_points

    def display_results(self):
       
        print(f"Out of {self.num_points} generated points, {len(self.points_in_triangle)} fell inside the right triangle.")
        print(f"Estimated area of the right triangle: {self.area:.4f}")

    def visualization(self):
        
        triangle_points = np.array([
            [0, 0],  # Starting point of the triangle
            [1, 0],  # The other end of the base of the triangle
            [1, 1],  # Height of triangle
            [0, 0],  # Return to starting point to close triangle
        ])

        square_points = np.array([
            [0, 0],  # Left-bottom of square
            [1, 0],  # Right-bottom of square
            [1, 1],  # Right-top of square
            [0, 1],  # Left-top of square
            [0, 0]   # Left-bottom again to close the square
        ])

        fig, ax = plt.subplots(figsize=(15, 8))
        
        ax.plot(square_points[:, 0], square_points[:, 1], marker="", color="#7457b3", alpha=1, label="Unit Square")
        ax.plot(triangle_points[:, 0], triangle_points[:, 1], marker="", color="#78bce3", alpha=0.8, label="Right Triangle")
        
        ax.scatter(self.all_points[:, 0], self.all_points[:, 1], color="#7aff83", s=1, label="Points Out of Triangle")
        ax.scatter(self.points_in_triangle[:, 0], self.points_in_triangle[:, 1], color="#dcccff", s=1, label="Points in Triangle")
        
        ax.set_title("Monte Carlo Simulation: Area of Right Triangle in Unit Square", fontsize=17, color="#393d47", weight = "bold")
        
        
        fig.text(0.5, 0.03, 
                    f"Estimated area of the right triangle: {self.area:.4f}\n"
                    f"Out of {self.num_points} generated points, {len(self.points_in_triangle)} fell inside the right triangle.", 
                    ha="center", fontsize=12, color="#393d47")
        
        plt.legend()
        plt.show()

    def run(self):
    
        self.monte_carlo_triangle_area()
        self.display_results()
        self.visualization()


def main():
    try:
        num_points= int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_points < 100000:
            num_points = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_points = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    app = Triangle(num_points = num_points)
    app.run()


if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt

"""
Monte Carlo simulation to estimate the value of π using random points.
- Generates random points in a [-1,1] x [-1,1] square.
- Counts how many points fall inside the unit circle.
- Uses the ratio of inside points to total points to approximate π.
- Visualizes the simulation results with a scatter plot.
"""

class MonteCarloPi:
    def __init__(self, num_points=10000):
        
        self.num_points = num_points
        self.inside_circle = 0  # Count of points inside the unit circle
        self.points = None  # Store generated points
        self.estimated_pi = 0  # Store estimated π value

    def monte_carlo_pi(self):
        
        x = np.random.uniform(-1, 1, self.num_points)
        y = np.random.uniform(-1, 1, self.num_points)
        distances = np.sqrt(x**2 + y**2)
        self.inside_circle = np.sum(distances <= 1)
        self.points = (x, y)
        self.estimated_pi = (self.inside_circle / self.num_points) * 4

    def display_results(self):
        
        error = abs((self.estimated_pi - np.pi) / np.pi) * 100  # Error percentage
        print(f"Estimated π: {self.estimated_pi:.6f}")
        print(f"Actual π: {np.pi:.6f}")
        print(f"Error: {error:.6f}%")

    def visualization(self):
        
        x, y = self.points
        inside = (x**2 + y**2) <= 1
        fig = plt.figure(figsize=(15,8))
        plt.scatter(x[inside], y[inside], color="#7aff83", s=1, label='Points Inside Circle')
        plt.scatter(x[~inside], y[~inside], color="#7ecefc", s=1, label="Points Outside Circle")
        circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
        plt.gca().add_patch(circle)
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.gca().set_aspect("equal", adjustable="datalim")
        plt.title("Monte Carlo Simulation: Estimate π", fontsize=17, color="#393d47", weight="bold")
        plt.legend()
        plt.grid(True)
        
        # Add estimated π value and error percentage as text on the plot
        fig.text(0.5, 0.02, f"Estimated π: {self.estimated_pi:.6f}\nActual π: {np.pi:.6f}\nError: {abs((self.estimated_pi - np.pi) / np.pi) * 100:.6f}%",
                 fontsize=12, color="#393d47", ha="left")
        
        plt.show()

    def run(self):
        self.monte_carlo_pi()
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
    
    app = MonteCarloPi(num_points=num_points)
    app.run()

if __name__ == "__main__":
    main()

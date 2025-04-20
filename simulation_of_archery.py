import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
🏹 Monte Carlo Archery Simulation 🏹

This simulation estimates the probability of hitting a circular target 
placed at the center of a square field using the Monte Carlo method.

Key Features:
- Randomly simulates arrow shots within the square.
- Calculates the probability of hitting the circular target.
- Visualizes hit vs. miss with a scatter plot and shows convergence.
- Demonstrates the geometric relationship between circle and square.

Expected Outcome:
- As the number of arrows increases, the empirical hit rate should converge 
  to the theoretical value (Area of Circle / Area of Square = πr² / (2r)² = π/4 ≈ 0.7854)

📌 Note: np.random.seed is set for reproducibility.
"""

class ArcherySimulation:
    def __init__(self, num_arrows):
        self.num_arrows = num_arrows

    def monte_carlo_archery(self):
        np.random.seed(42)
        self.radius = 1  # Radius of the circular target
        self.hits = 0
        
        self.x_hit, self.y_hit = [], []
        self.x_miss, self.y_miss = [], []

        # Simulate arrows being shot randomly in a square from -1 to 1 (width = 2r)
        for _ in range(self.num_arrows):
            x = np.random.uniform(-self.radius, self.radius)
            y = np.random.uniform(-self.radius, self.radius)

            distance = x**2 + y**2  # squared distance from center (0,0)

            if distance <= self.radius**2:
                self.hits += 1
                self.x_hit.append(x)
                self.y_hit.append(y)
            else:
                self.x_miss.append(x)
                self.y_miss.append(y)
        
        self.hit_probability = self.hits / self.num_arrows

    def calculate_error_margin(self, confidence=0.95):
        z = 1.96 if confidence == 0.95 else 1.64
        p = self.hit_probability
        n = self.num_arrows
        self.error_margin = z * np.sqrt((p * (1 - p)) / n)
    
    def display_result(self):
        print("\n🏹 Monte Carlo Archery Simulation Result 🏹")
        print(f"Total Arrows Shot: {self.num_arrows}")
        print(f"Arrows Hit Target: {self.hits}")
        print(f"Empirical Hit Probability: {self.hit_probability:.4f}")
        print(f"Theoretical Probability (π/4): {np.pi/4:.4f}")
        print("\n🔍 Note: As the number of arrows increases, the experimental probability should converge to π/4 (≈0.7854).")

    def visualization(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.scatter(self.x_hit, self.y_hit, color="#81f7b2", s=1, label="Hits")
        ax.scatter(self.x_miss, self.y_miss, color="#f78181", s=1, label="Misses")
        
        # Draw the circular target
        circle = plt.Circle((0, 0), self.radius, color="#6c7ae0", fill=False, linewidth=2, label="Target")
        ax.add_patch(circle)

        ax.set_title("Monte Carlo Archery Simulation", fontsize=16, color="#333333", weight="bold")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.legend(loc="upper right")
        ax.grid(True)
        ax.set_aspect("equal")
        fig.text(
            0.5, 0.05,
            f"Theoretical Probability (π/4): {np.pi/4:.4f} | Estimated Probability: {self.hit_probability:.4f} | Error Margin: {self.error_margin:.6f}",
            ha="center", fontsize=12, color="#555555"
        )
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):
        self.monte_carlo_archery()
        self.display_result()
        self.calculate_error_margin()
        self.visualization()


def main():
    try:
        num_arrows = int(input("Please enter the number of arrows (minimum 10,000): "))
        if num_arrows < 10000:
            num_arrows = 10000
            print("Warning: Sample size increased to 10,000 for better accuracy.")
    except:
        num_arrows = 10000
        print("Warning: Invalid input detected. Defaulting to 10,000 arrows.")

    simulation = ArcherySimulation(num_arrows)
    simulation.run()


if __name__ == "__main__":
    main()

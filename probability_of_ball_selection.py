import numpy as np
import matplotlib.pyplot as plt

"""
🎯 Monte Carlo Ball Selection Simulation 🎯

🔹 Goal:
   - Simulates drawing balls of different colors from a mixed set.
   - Estimates the probability of drawing a specific color.
   - Uses Monte Carlo methods to approximate the theoretical probability.

📊 How It Works:
   - Defines a bag of balls with different colors and counts.
   - Randomly selects balls and tracks how often a specific color appears.
   - Computes and visualizes the probability distribution.
"""

class BallSelectionSimulator:
    def __init__(self, trials, target_color, colors):
        """
        Initializes the simulation with user-defined number of trials, target color, and ball distribution.
        """
        self.trials = trials
        self.target_color = target_color.capitalize()
        self.colors = colors  
        self.total_balls = sum(self.colors.values())
        self.selection_count = 0
        self.probability = 0

    def monte_carlo_simulation(self):
        
        try:
            all_balls = [color for color, count in self.colors.items() for _ in range(count)]
            np.random.shuffle(all_balls)
            selections = np.random.choice(all_balls, self.trials, replace=True)
            self.selection_count = np.sum(selections == self.target_color)
            self.probability = self.selection_count / self.trials
        except Exception as e:
            print(f"Error during simulation: {e}")

    def display_result(self):
        print(f"\n🔹 Total Balls in the Bag: {self.total_balls}")
        print(f"🎨 Color Distribution: {self.colors}")
        print(f"🎯 Target Color: {self.target_color}")
        print(f"🎲 Total Trials: {self.trials}")
        print(f"✅ {self.target_color} was drawn {self.selection_count} times.")
        print(f"📊 Estimated Probability: {self.probability:.4f}")

    def visualize(self):
        
        try:
            colors = ["#81a4f7","#a8f781", "#b081f7"]
            
            fig, ax = plt.subplots(1, 2, figsize=(14, 6))
            
            ax[0].bar(self.colors.keys(), self.colors.values(), color= colors[0])
            ax[0].set_title("Ball Distribution in the Bag", fontsize=14)
           
            ax[0].grid(axis="y", linestyle="--", alpha=0.7)
            ax[0].set_axisbelow(True)

            
            data = [self.probability, 1 - self.probability]
            labels_pie = [f"{self.target_color}: {self.probability:.2%}", "Other Colors"]
            ax[1].pie(data, labels=labels_pie, colors=colors, autopct="%1.1f%%", startangle=90)
            ax[1].set_title(f"Probability of Drawing {self.target_color}", fontsize=14)

            fig.suptitle("Monte Carlo Ball Selection Simulation", fontsize=16, fontweight="bold")
            fig.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Visualization error: {e}")

    def run(self):
        
        self.monte_carlo_simulation()
        self.display_result()
        self.visualize()


def main():
    """
    Initializes and runs the ball selection simulation with user input.
    """
    try:
        num_draw= int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_draw < 100000:
            num_draw = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_draw= 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    try:
        colors = {}
        num_colors = int(input("Enter the number of different ball colors: "))
        for _ in range(num_colors):
            color_name = input("Enter color name: ").capitalize().strip()
            count = int(input(f"Enter the number of {color_name} balls: "))
            colors[color_name] = count

        target_color = input("Enter the target color: ").capitalize().strip()
        if target_color not in colors:
            raise ValueError("Invalid color! Please choose a color from the entered list.")

        app = BallSelectionSimulator(num_draw, target_color, colors)
        app.run()

    except ValueError as e:
        print(f"🚨 Input Error: {e}. Restarting with default values.")
        app = BallSelectionSimulator(100000, "Red", {"Red": 30, "Blue": 50, "Green": 20})
        app.run()


if __name__ == "__main__":
    main()

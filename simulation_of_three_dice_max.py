import numpy as np
import matplotlib.pyplot as plt

"""
Monte Carlo Simulation: Highest of 3 Dice Being 5 or 6 🎲🎲🎲

This program simulates rolling three six-sided dice multiple times (default: 100,000 rolls)
and estimates the probability that the highest value among the three is either 5 or 6.

How It Works:
- Three dice are rolled in each trial.
- The maximum value from the three is recorded.
- The program counts how often the highest roll is 5 or 6.
- The estimated probability is calculated using Monte Carlo methods.

Visualization:
📊 A bar chart displays the frequency of occurrences.
🥧 A pie chart illustrates the probability distribution.

This simulation provides insights into probability distributions and randomness in dice rolls.
"""

class ThreeDiceSimulation:
    
    def __init__(self, num_rolls=100000):
        
        self.num_rolls = num_rolls
        self.success_count = 0
        self.probability = 0
    
    def monte_carlo_dice(self):
        
        np.random.seed(100)
        rolls = np.random.randint(1, 7, size=(self.num_rolls, 3))  
        max_rolls = np.max(rolls, axis=1)  
        self.success_count = np.sum((max_rolls == 5) | (max_rolls == 6))  
        self.probability = self.success_count / self.num_rolls  
        
    def display_result(self):

        print(f"Out of {self.num_rolls} rolls, the highest die was 5 or 6 in {self.success_count} cases.")
        print(f"Estimated probability: {self.probability:.4f}")
    
    def visualization(self):
        
        labels = ["Max Roll is 5 or 6", "Max Roll is 1-4"]
        values = [self.success_count, self.num_rolls - self.success_count]
        colors = ["#81a4f7","#a8f781", "#b081f7"]
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 7))
        
        axes[0].bar(labels, values, color=colors)
        axes[0].set_title("Frequency of Maximum Roll Being 5 or 6", fontsize=14, color="#393d47")
        axes[0].set_ylabel("Count")
        axes[0].grid(axis="y")
        
        axes[1].pie(values, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90,
                    textprops={'color': "#393d47", 'fontsize': 12})
        axes[1].set_title("Probability Distribution", fontsize=14, color="#393d47")
        
        fig.suptitle("Monte Carlo Simulation: Highest of 3 Dice Being 5 or 6", fontsize=16, fontweight="bold")
        
        fig.text(
            0.5,
            0.05,
            f"Out of {self.num_rolls} rolls, the highest die was 5 or 6 in {self.success_count} cases.\n"
            f"Estimated probability: {self.probability:.4f}", 
            ha="center", va="bottom", fontsize=14, color="#393d47")
        
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.2, hspace=0.4)
        plt.show()
    
    def run(self):
        self.monte_carlo_dice()
        self.display_result()
        self.visualization()


def main():
    try:
        num_rolls = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_rolls < 100000:
            num_rolls = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_rolls = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    app = ThreeDiceSimulation(num_rolls)
    app.run()

if __name__ == "__main__":
    main()

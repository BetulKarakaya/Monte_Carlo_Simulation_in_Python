import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
🎲 Monte Carlo Dice Sum Probability Simulation 🎲

This program simulates rolling two dice multiple times and estimates 
the probability of their sum being a specific value using the 
Monte Carlo method. 

Key Features:
- Uses **NumPy's random integer generation** to simulate dice rolls.
- Rolls **100,000** dice pairs (default) for high accuracy.
- **Counts occurrences** where the sum of two dice equals a given target.
- **Computes probability** as (successful cases) / (total rolls).
- **Visualizes results** using a **pie chart**.

Monte Carlo Method Criteria:
✅ Randomness (np.random.randint ensures unbiased rolls)  
✅ Large Sample Size (100,000 trials for accuracy)  
✅ Independent Trials (Each dice roll is independent)  
✅ Probability Approximation (Empirical estimation vs. theoretical probability)  

This approach helps illustrate real-world probability estimation when theoretical 
calculations are difficult or require validation.

"""

class  RollingTheDie:
    
    def __init__(self, num_rolls = 100000,total_sum = 8):

        self.num_rolls = num_rolls
        self.total_sum = total_sum
        
    
    def monte_carlo_dice(self):
        roll1 = np.random.randint(1, 7, size= self.num_rolls)
        roll2 = np.random.randint(1, 7, size= self.num_rolls)
        self.df = pd.DataFrame(np.vstack((roll1,roll2)).T)
        self.df.rename(columns={0:"FirstDie", 1:"SecondDie"}, inplace = True)
        self.sum = self.df[self.df["FirstDie"] + self.df["SecondDie"] == self.total_sum].shape[0]

        self.probability = self.sum / self.num_rolls

    def display_result(self):
        print(f"Out of {self.num_rolls} rolls of dice pairs, the sum of the dice is {self.total_sum} in {self.sum} cases.")
        print(f"Probability of rolling a 6: {self.probability:.4f}")

    def visualization(self):

        data = np.array([self.probability, 1 - self.probability])
        colors = ["#3307f7","#9681f7"]
        labels = [f"Chance of getting a sum of {self.total_sum}: P({self.total_sum})", 
                  f"Chance of not getting {self.total_sum}: 1 - P({self.total_sum})"]
        
        plt.figure(figsize = (12,5))
        plt.pie(data, labels= labels, colors = colors)
        plt.title(f"Probability of Rolling a Sum of {self.total_sum}", color = "#1d1b26", fontsize = 15, weight = "bold")
        plt.suptitle(f"A total of {self.num_rolls} pairs of dice were rolled. Out of these, {self.sum} pairs had a sum of {self.total_sum}", color = "#1d1b26", fontsize = 14)
        plt.show()

    def run(self):
        self.monte_carlo_dice()
        self.display_result()
        self.visualization()
        
def main():
    app = RollingTheDie()
    app.run()

if __name__ == "__main__":
    main()
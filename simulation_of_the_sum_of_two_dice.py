import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
🎲 Monte Carlo Dice Sum Probability Simulation 🎲

This program simulates rolling two dice multiple times and estimates 
the probability of their sum being a specific value using the 
Monte Carlo method.

Key Features:
- Uses **NumPy's random integer generation** to simulate rolls of two six-sided dice.
- Rolls **100,000** dice pairs (default) for high accuracy.
- **Counts occurrences** where the sum of the dice equals a given target value.
- **Computes the probability** of getting the target sum as (successful cases) / (total rolls).
- **Visualizes results** using a **pie chart** to represent the probability and its complement.

Error Handling:
- Ensures that the number of rolls is at least 100,000 and that the dice sum is between 2 and 12.
- Provides default values if invalid input is detected.
"""

class  RollingTheDie:
    
    def __init__(self, num_rolls = 100000, total_sum = 8):

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
        colors = ["#81a4f7","#a8f781"]
        labels = [f"Chance of getting a sum of {self.total_sum}: P({self.total_sum})", 
                  f"Chance of not getting {self.total_sum}: 1 - P({self.total_sum})"]
        
        fig, ax = plt.subplots(figsize = (12,5))
        ax.pie(data, labels= labels, colors = colors, autopct="%1.1f%%")
        plt.title(f"Probability of Rolling a Sum of {self.total_sum}", color = "#393d47", fontsize = 17)
        plt.text(0.5, .1, f"A total of {self.num_rolls} pairs of dice were rolled. Out of these, {self.sum} pairs had a sum of {self.total_sum}", ha = "center", fontsize = 14, color = "#393d47", transform= fig.transFigure)
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
        num_rolls= 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    try:
        total_sum = int(input("Please enter a number for the sum of the rolled dice pairs: "))
        if total_sum < 2 or total_sum > 12:
            print("Warning: The sum of the dice must be greater than or equal two and less than or equal to 12. The default value of 8 has been assigned for the dice sum.")
            total_sum = 8
    except:
        print("Warning: The sum of the dice must be greater than zero and less than or equal to 12. The default value of 8 has been assigned for the dice sum.")
        total_sum = 8
    
    app = RollingTheDie(num_rolls = num_rolls, total_sum = total_sum)
    app.run()

if __name__ == "__main__":
    main()
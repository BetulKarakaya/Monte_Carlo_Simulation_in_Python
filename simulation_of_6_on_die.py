import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 

"""
Monte Carlo Simulation: Probability of Rolling a 6 on a Die

This program simulates rolling a six-sided die multiple times (default: 100,000 rolls) 
and estimates the probability of rolling a 6. 

How It Works:
- Rolls a fair six-sided die for a specified number of times.
- Counts how many times the outcome is a 6.
- Computes the experimental probability of rolling a 6.
- Displays the results numerically and visually using a bar chart.
- Demonstrates the Law of Large Numbers, showing how the probability converges to the expected theoretical value (1/6 ≈ 16.67%) as the sample size increases.

Visualization:
📊 A bar chart representing the frequency of each die face.
📌 Text summary displaying the probability and count of rolling a 6.
"""

class Dice:
    def __init__(self,num_rolls):
        self.num_rolls = num_rolls
        

    def monte_carlo_dice(self):
        self.rolls = np.random.randint(1, 7, size= self.num_rolls)  
        self.count_six = np.sum(self.rolls == 6)  
        self.probability = self.count_six / self.num_rolls 
        self.df = pd.DataFrame(np.array(self.rolls), columns = ["DiceSide"] )
        self.df = self.df.value_counts().reset_index().rename(columns={"count":"Count"}).sort_values(by = ["DiceSide"], ignore_index= True)

    def display_result(self):
        print(f"Out of {self.num_rolls} rolls, the number of times 6 appeared: {self.count_six}")
        print(f"Probability of rolling a 6: {self.probability:.4f}")

    
    def visualization(self):
        limit = math.ceil((self.df["Count"].max()) / 1000) * 1000
        fig, axes = plt.subplots(1,1, figsize = (15,8))
        axes.bar(self.df["DiceSide"], self.df["Count"], color = "#81a4f7")
        axes.set_title("Monte Carlo Simulation: The Probability Of Rolling A 6 On a Die", fontsize=16, color = "#393d47", weight = "bold")
        axes.set_yticks(np.arange(0, limit +1000, limit /20))
        axes.set_xticks([1, 2, 3, 4, 5, 6])
        axes.grid()
        axes.set_axisbelow(True)

        fig.text(
            0.5,
            0.05,
            f"Probability of Rolling a 6 on a Die is {self.probability}\n"
            f"Out of {self.num_rolls} rolls, the number of times 6 appeared: {self.count_six}", 
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
        num_rolls= 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    app = Dice(num_rolls)
    app.run()


if __name__ == "__main__":
    main()
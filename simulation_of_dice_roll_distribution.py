import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
🎲 Monte Carlo Dice Roll Simulation 🎲

This program simulates rolling a six-sided die a large number of times 
(100,000 by default) using the Monte Carlo method. It calculates the 
empirical probability of each face appearing and compares it with the 
expected theoretical probability (1/6 ≈ 16.67%).

Key Features:
- Simulates dice rolls and records frequency of each face.
- Computes and displays empirical vs. theoretical probabilities.
- Visualizes the distribution using a bar chart and pie chart.
- Demonstrates the Law of Large Numbers as the sample size increases.

Usage:
- The user can specify the number of rolls (minimum 100,000).
- The program outputs the frequency and probability of each face.
- Graphical representations help in visualizing the probability distribution.

Expected Outcome:
- As the number of rolls increases, the empirical probabilities should 
  converge to the theoretical value (≈16.67%) for each face.

📌 Note: The randomness is controlled using np.random.seed(100) to ensure 
reproducibility of results.
"""


class Dice:
    def __init__(self,num_rolls):
        self.num_rolls = num_rolls
        

    def monte_carlo_dice(self):
        np.random.seed(100)
        self.rolls = np.random.randint(1, 7, size= self.num_rolls)  # Rolling the dice (between 1 and 6)
        self.df = pd.DataFrame(np.array(self.rolls))
        self.df = self.df.value_counts().reset_index().rename(columns={0: "DiceSide", "count":"Count"}).sort_values(by = ["DiceSide"], ignore_index= True)
        self.df["Probability"] = self.df["Count"]/ self.num_rolls

    def display_result(self):
        """ Display the simulation results in a readable format """
        print("\n🎲 Monte Carlo Dice Roll Simulation Results 🎲")
        print(f"Total Rolls: {self.num_rolls}\n")

        # Print each face count and probability
        for index, row in self.df.iterrows():
            expected_prob = 1/6  # Theoretical probability for a fair die
            print(f"Face {int(row['DiceSide'])}: Rolled {int(row['Count'])} times, Probability: {row['Probability']:.4f} "
                f"(Expected: {expected_prob:.4f})")

        print("\n🔍 Note: As the number of rolls increases, the experimental probabilities should converge to the theoretical value (≈16.67%).")

        
    def visualization(self):
        
        colors = ["#81a4f7","#a8f781", "#b081f7"]
        fig, axes = plt.subplots(1, 2, figsize = (15,8))
       
        axes[0].bar(self.df["DiceSide"], self.df["Count"], color = colors[0])
        
        axes[0].set_title("Monte Carlo Dice Simulation", fontsize=16, color = "#393d47")
        axes[0].set_xticks([1, 2, 3, 4, 5, 6])
        axes[0].set_yticks(np.arange(0,max(self.df["Count"]+1000),1000))
        axes[0].grid()
        axes[0].set_axisbelow(True)

        axes[1].pie(self.df["Probability"], labels= self.df["DiceSide"], colors = colors , autopct="%1.1f%%",  textprops={'color':"#393d47", 'fontsize': 12}, startangle = 90)
        axes[1].set_title("Probability Distribution of Each Face of the Die", fontsize = 16, color = "#393d47")
        line = plt.Line2D((.5,.5),(.1,.92), color = "#6b6c6e", linewidth = 2, linestyle = "--")
        fig.add_artist(line)
        fig.tight_layout(pad=7.0)
        
        fig.suptitle("Monte Carlo Simulation: Probability Distribution of Dice Faces", fontsize = 18, color = "#393d47", weight = "bold")
        
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
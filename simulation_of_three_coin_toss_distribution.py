import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Monte Carlo Simulation: Probability of Getting at Least One 'Tails' in Three Coin Tosses

This simulation estimates the probability of getting at least one 'Tails' 
when flipping three fair coins per trial.

Key Steps:
1. Generate random coin toss results for a large number of trials (default: 100,000).
2. Store results in a Pandas DataFrame and count occurrences of 'Tails'.
3. Calculate the probability of getting at least one 'Tails' by dividing the 
   number of successful trials by the total number of trials.
4. Display the results in text format.
5. Visualize the results using:
   - A bar chart showing how many times 'Heads' and 'Tails' appeared in each coin toss.
   - A pie chart illustrating the probability distribution.

Theoretical Probability Calculation:
Mathematically, the probability of getting at least one 'Tails' in three coin tosses is:

    P(At least one Tails) = 1 - P(No Tails)
                           = 1 - (1/2 × 1/2 × 1/2)
                           = 1 - 1/8
                           = 7/8 ≈ 0.875 (87.5%)

If the simulation is implemented correctly, it should yield an approximate probability of 0.875. 🎯
"""


class ThreeCoinToss:
    def __init__(self, num_toss = 100000):
        self.num_toss = num_toss
        self.at_least_one_tails = None
        self.probability = 0
    
    def monte_carlo_toss(self):
        np.random.seed(100)

        self.all_toss = np.random.choice(["Heads","Tails"], size = (self.num_toss,3))
        self.df = pd.DataFrame(self.all_toss, columns=["First", "Second", "Third"])
        self.at_least_one_tails = self.df[(self.df["First"] == "Tails" ) | (self.df["Second"] == "Tails" ) | (self.df["Third"] == "Tails")]
        self.probability = len(self.at_least_one_tails) / self.num_toss

    def display_results(self):
        print(f"Out of {self.num_toss} trials, at least one 'Tails' appeared in {len(self.at_least_one_tails)} cases.")
        print(f"Estimated Probability: {self.probability:.4f}")

    def visualization(self):
        label = ["Heads", "Tails"]
        colors = ["#81a4f7","#a8f781", "#b081f7"]
        N = 2
        ind = np.arange(N)  
        width = 0.25
        fig, axes = plt.subplots(1, 2, figsize = (15,8))
        axes[0].bar(ind,self.df["First"].value_counts(), width = width, color= colors[0])
        axes[0].bar(ind+width,self.df["Second"].value_counts(), width = width, color= colors[1])
        axes[0].bar(ind+width*2,self.df["Third"].value_counts(), width = width, color= colors[2])
        axes[0].set_xticks(ind+width,label)
        axes[0].set_yticks(np.arange(0,self.num_toss/2 +1000, self.num_toss/20))
        axes[0].grid()
        axes[0].set_axisbelow(True)
        axes[0].legend(["First Coin","Second Coin ","Third Coin"])
        
        axes[1].pie([self.probability, 1 - self.probability],  labels= ["At Least One Tails", "No Tails"], colors = colors , autopct="%1.1f%%",  textprops={'color':"#393d47", 'fontsize': 12}, startangle = 90)
        axes[1].set_title("Probability Distribution of Getting at Least One 'Tails' in Three Coin Tosses", fontsize = 14, color = "#393d47")
        line = plt.Line2D((.5,.5),(.1,.92), color = "#6b6c6e", linewidth = 2, linestyle = "--")
        fig.add_artist(line)
        fig.tight_layout(pad=7.0)
        
        fig.suptitle("Monte Carlo Simulation: Probability of Getting at Least One Tails", fontsize = 17, color = "#393d47", weight = "bold")
        fig.text(0.5, 0.05,f"Out of { self.num_toss} sets of three coin tosses, Tails appeared at least once in {len(self.at_least_one_tails)} cases. Probability: {self.probability}" , ha = "center", fontsize = 14, color = "#393d47")
        plt.show()
    
    
    def run(self):
        self.monte_carlo_toss()
        self.display_results()
        self.visualization()

def main():
    try:
        num_toss = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))

        if (num_toss < 100000):
            num_toss = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_toss = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    app = ThreeCoinToss(num_toss = num_toss)
    app.run()

if __name__ == "__main__":
    main()
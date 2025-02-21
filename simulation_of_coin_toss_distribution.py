import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""
Monte Carlo Coin Toss Simulation

This program simulates a large number of coin flips using Monte Carlo methods 
to estimate the probability of getting heads or tails. It follows these steps:

1. **Random Sampling:** Uses `np.random.choice()` to simulate a given number of coin flips.
2. **Probability Calculation:** Computes the frequency of heads and tails.
3. **Visualization:** Generates:
   - A pie chart showing the probability distribution.
   - A bar chart displaying the total occurrences of heads and tails.
4. **User Input Handling:** Allows the user to specify the number of flips (default: 100,000).
5. **Error Handling:** If invalid input is given, it defaults to 100,000 flips.

This simulation demonstrates the **Law of Large Numbers**, as the probability should converge 
to 50% for each outcome when the sample size is large enough.

"""

class CoinToss:

    def __init__(self, num_flip = 100000):
        self.num_flip = num_flip


    def monte_carlo_flip(self):
        np.random.seed(100)
        self.all_flips = np.random.choice(["Heads","Tails"], self.num_flip)
        self.heads = np.sum(self.all_flips == "Heads")
        self.tails = np.sum(self.all_flips == "Tails")
        self.heads_probability = self.heads / self.num_flip
        self.tails_probability = self.tails / self.num_flip

    def display_result(self):
        self.text = f"""In {self.num_flip} coin flips, heads appeared {self.heads} times and tails appeared {self.tails} times.\nThe probability distribution shows that heads occurred in %{self.heads_probability} of the flips, while tails appeared in %{self.tails_probability} of the cases."""
        print(self.text)
        

    def visualization(self):
        
        fig, ax = plt.subplots(1,2, figsize=(12, 8))
        
        data= np.array([self.heads_probability, self.tails_probability])
        labels = ["Heads", "Tails"]
        colors = ["#81a4f7","#a8f781"]
        ax[0].pie(data, labels= labels, colors = colors , autopct="%1.1f%%",  textprops={'color':"#393d47", 'fontsize': 12}, startangle = 90)
        ax[0].set_title("Heads and Tails Distribution", fontsize = 15, color = "#393d47")
        
        ax[1].bar(["Heads","Tails"],[self.heads, self.tails], color = colors)
        ax[1].set_title("Distribution of Heads and Tails in Coin Tosses", fontsize = 15, color = "#393d47")
        ax[1].set_yticks(np.arange(0,max(self.heads, self.tails)+500, self.num_flip /20))
        ax[1].grid()
        ax[1].set_axisbelow(True)
        
        line = plt.Line2D((.5,.5),(.1,.90), color = "#6b6c6e", linewidth = 1, linestyle = "--")
        fig.add_artist(line)
        fig.tight_layout(pad=7.0)
        
        fig.suptitle("Monte Carlo Coin Toss Simulation",fontsize = 17, color = "#393d47", weight = "bold")
        fig.text(0.5, 0.02, self.text, ha = "center", fontsize = 12, color = "#393d47")

        plt.show()

    def run(self):
        self.monte_carlo_flip()
        self.display_result()
        self.visualization()

def main():
    try:
        num_flip = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))

        if (num_flip < 100000):
            num_flip = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_flip = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    app = CoinToss(num_flip = num_flip)
    app.run()

if __name__ == "__main__":
    main()
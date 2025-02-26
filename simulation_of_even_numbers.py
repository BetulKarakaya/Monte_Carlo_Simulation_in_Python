import matplotlib.pyplot as plt
import numpy as np

"""
Monte Carlo Simulation: Estimating the Probability of Even Numbers in a Given Range

Description:
This program estimates the probability of randomly selecting an even number from a user-defined range 
using the Monte Carlo method. It generates a large number of random integers within a specified range 
and calculates the proportion of even numbers.

How It Works:
- The user inputs the lower and upper bounds of the number space [min, max).
- The user specifies the total number of random numbers to be generated.
- The program randomly generates numbers within the given range.
- It determines how many of these numbers are even.
- The probability of selecting an even number is calculated as:
  P(even) = (Number of even numbers) / (Total generated numbers)
- The results are displayed numerically and visualized using bar and pie charts.

Features:
✔ User-defined input for number space and sample size with error handling.
✔ Automatic adjustment to default values in case of invalid input.
✔ Visualization of probability distribution using Matplotlib.
✔ Demonstrates the Law of Large Numbers by converging to the expected probability.

This simulation provides insights into probability estimation and random sampling, useful for applications 
in data science, statistics, and probability theory!
"""


class EvenNumber:

    def __init__(self, num_samples, space ):

        self.num_samples = num_samples
        self.min_space = space["Min"]
        self.max_space = space["Max"]
        self.probability = 0

    def monte_carlo_even_numbers(self):

        np.random.seed(100)
        self.all_numbers = np.random.randint(self.min_space, self.max_space, size = self.num_samples)
        self.all_even = sum(1 for x in self.all_numbers if x % 2 == 0)
        self.probability = self.all_even / self.num_samples

    def display_results(self):

        print(f"Sample range is [{self.min_space}, {self.max_space}).")
        print(f"Out of {self.num_samples} numbers {self.all_even} is even number.")
        print(f"Probability of having a even number in sample space is {self.probability}")

    def visualization(self):

        colors = ["#81a4f7","#a8f781"]
        labels = ["Even Numbers", "Odd Numbers"]
        values = [self.all_even, self.num_samples - self.all_even]
        
        fig, axes = plt.subplots(1,2, figsize = (15,8))
        
        axes[0].bar(labels, values, color = colors)
        axes[0].set_yticks(np.arange(0,max(values), self.num_samples /20))
        axes[0].grid()
        axes[0].set_axisbelow(True)
        axes[0].set_title("Total Count Of Odd And Even Numbers In The Example", color = "#393d47", fontsize = 14)

        axes[1].pie([self.probability, 1- self.probability], labels = labels, colors = colors, autopct = "%1.2f%%", textprops={'color':"#393d47", 'fontsize': 13}, startangle = 90)
        axes[1].set_title("Probabilty Analysis", color = "#393d47", fontsize = 15)

        fig.suptitle("Monte Carlo Simulation: Probability Of Even Numbers In Sample", color = "#393d47", fontsize = 18, weight = "bold")

        line = plt.Line2D((.5,.5),(.15,.9),linestyle = "--", linewidth = 2, color = "grey")
        fig.add_artist(line)
        
        fig.text(
            0.5,
            0.05,
            f"Sample range is [{self.min_space}, {self.max_space}).\n"
            f"Out of {self.num_samples} numbers {self.all_even} is even number.\n"
            f"Probability of having a even number in sample space is {self.probability}",
            ha="center", va="bottom", fontsize=14, color="#393d47"
        )

        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):

        self.monte_carlo_even_numbers()
        self.display_results()
        self.visualization()


def control(min_space, max_space):
    
    if min_space >= max_space:
        return False
    return True

def main():

    try:
        min_space = int(input("Enter the lower limit of the number space: "))  
        max_space = int(input("Enter the upper limit of the number space: ")) 

        if(control(min_space= min_space, max_space = max_space)):
            space = {"Min": min_space, "Max": max_space}
        else:
            raise ValueError()
    except:
        print("Warning: A non-numeric input was detected, so default space and range have been adjusted to: ")
        print("Space = [0,100)")

        space = {"Min": 0, "Max": 100}

    try:
        num_samples = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_samples < 100000:
            num_samples = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_samples = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")

    app = EvenNumber(space = space, num_samples = num_samples)
    app.run()

if __name__ == "__main__":
    main()
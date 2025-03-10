import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

# This class simulates the rolling of three six-sided dice a specified number of times 
# and calculates the probability that all three dice will roll greater than a specified minimum value.
# It also visualizes the probability distribution, displays the results of the simulation, 
# and compares the simulated probability with the theoretical probability.
# The simulation is performed using a Monte Carlo method where random dice rolls are generated.
# The results are displayed using a pie chart to show the proportion of rolls greater and smaller than the minimum value,
# and bar plots are used to display the distribution of outcomes for each die separately.
# Additionally, the error between the simulated probability and the theoretical probability is calculated and displayed.

class ThreeDiceRoll:
    def __init__(self, num_rolls, min_value):
        self.num_rolls = num_rolls
        self.probability = 0
        self.min_value = min_value

    def monte_carlo_coin_toss(self):
       
        self.all_rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=(self.num_rolls, 3))
        # Find all rolls where all dice have values greater than min_value
        self.all_bigger_than = self.all_rolls[np.all(self.all_rolls > self.min_value, axis=1)]
        self.probability = len(self.all_bigger_than) / self.num_rolls
        self.df = pd.DataFrame(self.all_rolls, columns=["First", "Second", "Third"])
       

    def display_results(self):
        
        theoretical_probability = ((6 - self.min_value) / 6) ** 3
        error = abs(self.probability - theoretical_probability) * 100  # Error in percentage
        print(f"The Probability from Simulation is {self.probability:.5f}")
        print(f"The Theoretical Probability is {theoretical_probability:.5f}")
        print(f"Error between the theoretical and simulated probability is {error:.2f}%")

    def visualization(self):
        colors = ["#81a4f7", "#a8f781", "#b081f7", "#faa946"]
        labels = [f"Probability of Not Bigger Than {self.min_value}", f"Probability of Bigger Than {self.min_value}"]
        x_axis = np.arange(1, 7, 1)  

        fig = plt.figure(figsize=(15, 8))
        spec = gridspec.GridSpec(1, 2, width_ratios=[1, 2])  

        ax_pie = fig.add_subplot(spec[0])
        ax_pie.pie(
            [1 - self.probability, self.probability], 
            colors=colors, 
            labels=labels, 
            autopct="%1.2f%%",
            textprops={'color': "#393d47", 'fontsize': 12}, 
            startangle=90
        )
        ax_pie.set_title(f"The probability distribution of all three dice rolling greater than {self.min_value}", fontsize = 13,color="#393d47")

        # Right part (3 subplots, dividing vertically)
        spec_right = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=spec[1])  # Right side divided into 3 rows
        dice_labels = ["First Die", "Second Die", "Third Die"]
        axes_right = [fig.add_subplot(spec_right[i]) for i in range(3)]  # 3 subplots for dice

        # Create bar plots for each dice
        for i, ax in enumerate(axes_right):
            counts = self.df.iloc[:, i].value_counts().sort_index()
            ax.bar(x_axis, counts, color=colors[i])
            ax.set_xticks(x_axis)
            ax.set_yticks(np.arange(0, max(counts) + 1000, max(counts) / 10))
            ax.set_title(dice_labels[i])
            ax.grid()
            ax.set_axisbelow(True)
            if i < 2:
                ax.set_xticklabels([])  # Remove x-tick labels for the first two plots

        # Adding x-axis label to the last subplot
        axes_right[-1].set_xlabel("Dice Roll Outcome")

       
        fig.suptitle(f"Monte Carlo Simulation: Probability of Each Die Rolling Greater Than {self.min_value}", fontsize=18, color="#393d47", weight="bold")
        fig.text(0.5, 0.01, f"Theoretical Probability: {((6 - self.min_value) / 6) ** 3:.5f} | Simulated Probability: {self.probability:.5f} | Error: {abs(self.probability - ((6 - self.min_value) / 6) ** 3) * 100:.2f}%", 
                 ha='center', va='center', fontsize=12, color='#393d47')
        
        plt.tight_layout()
        plt.show()

    def run(self):
        self.monte_carlo_coin_toss()
        self.display_results()
        self.visualization()

    
def main():
    try:
        num_rolls = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_rolls < 100000:
            num_rolls = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except ValueError:
        num_rolls = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")

    try:
        min_value = int(input("Please enter a minimum value for the dice roll (1-6): "))
        if min_value < 1 or min_value > 6:
            min_value = 4  # Default value
            print("Warning: Invalid input for minimum value. The default minimum value of 4 has been set.")
    except ValueError:
        min_value = 4  # Default value
        print("Warning: A non-numeric input was detected for the minimum value, so the default minimum value of 4 has been set.")
    app = ThreeDiceRoll(num_rolls= num_rolls, min_value= min_value)
    app.run()

if __name__ == "__main__":
    main()

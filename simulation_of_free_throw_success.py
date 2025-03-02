import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Monte Carlo Simulation: Probability of Making at Least 7 Successful Free Throws

This simulation estimates the probability of a basketball player making at least 7 successful free throws out of 10 attempts.
- A player has a predefined success rate (default: 80%).
- Simulates a large number of free throw attempts.
- Uses Monte Carlo methods to estimate the probability.
- Visualizes the results using bar and pie charts.
"""

class FreeThrow:
   
    def __init__(self, num_repeat, success_rate):
        self.num_repeat = num_repeat
        self.success_rate = float(success_rate / 100)
        self.probability = 0

    def monte_carlo_free_throw(self):
       
        np.random.seed(100)
        self.all_throws = np.random.choice(2, (self.num_repeat, 10), p=[1 - self.success_rate, self.success_rate])
        self.successful_throws = np.sum(self.all_throws == 1, axis=1)
        self.df = (
            pd.DataFrame(self.successful_throws)
            .value_counts()
            .reset_index()
            .rename(columns={0: "Free Throw", "count": "Successful Throws"})
            .sort_values(by="Free Throw", ignore_index=True)
        )
        self.valid_samples_count = sum(self.successful_throws >= 7)
        self.probability = self.valid_samples_count / self.num_repeat

    def display_results(self):

        print(f"Out of {self.num_repeat} trials, {self.valid_samples_count} had at least 7 successful free throws.")
        print(f"Estimated probability: {self.probability:.4f}")
        print(f"Most common number of successes: {self.df.iloc[self.df['Successful Throws'].idxmax()]['Free Throw']}")
        print(f"Least common number of successes: {self.df.iloc[self.df['Successful Throws'].idxmin()]['Free Throw']}")
        print(f"Average successful free throws: {np.mean(self.successful_throws):.2f}")

    def visualization(self):
        
        colors = ["#81a4f7", "#a8f781", "#b081f7"]
        labels = ["6 or Fewer Free Throws", "At Least 7 Free Throws"]
        fig, axes = plt.subplots(1, 2, figsize=(17, 8))

        axes[0].pie(
            [1 - self.probability, self.probability],
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            textprops={"color": "#393d47", "fontsize": 12},
            startangle=90,
        )
        axes[0].set_title(
            "Probability of Making at Least 7 Successful Free Throws", fontsize=14, color="#393d47"
        )

        axes[1].bar(self.df["Free Throw"], self.df["Successful Throws"], color=colors[0])
        axes[1].grid()
        axes[1].set_axisbelow(True)
        axes[1].set_title(
            "Number of Successful Free Throws Out of 10 Attempts", fontsize=14, color="#393d47"
        )

        fig.suptitle(
            "Monte Carlo Simulation: Probability of Making At Least 7 Successful Free Throws",
            fontsize=17,
            color="#393d47",
        )
        
        line = plt.Line2D((.5, .5), (.2, .92), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line)

        fig.text(
            0.5,
            0.01,
            f"Out of {self.num_repeat} trials, {self.valid_samples_count} had at least 7 successful free throws.\n"
            f"Estimated probability: {self.probability:.4f}\n"
            f"Most common number of successes: {self.df.iloc[self.df['Successful Throws'].idxmax()]['Free Throw']}\n"
            f"Least common number of successes: {self.df.iloc[self.df['Successful Throws'].idxmin()]['Free Throw']}\n"
            f"Average successful free throws: {np.mean(self.successful_throws):.2f}\n",
            ha="center",
            va="bottom",
            fontsize=14,
            color="#393d47",
        )
        
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.4, hspace=0.4)
        plt.show()

    def run(self):
        self.monte_carlo_free_throw()
        self.display_results()
        self.visualization()


def main():
    try:
        num_repeat = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_repeat < 100000:
            num_repeat = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_repeat = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    try:
        success_rate = int(input("Enter the player's free throw success rate (0-100): "))
        if not (0 <= success_rate <= 100):
            success_rate = 80
            print("Warning: The success rate must be between 0 and 100. Defaulting to 80%.")
    except:
        success_rate = 80
        print("Warning: Invalid input detected, defaulting to 80%.")
    
    app = FreeThrow(num_repeat=num_repeat, success_rate=success_rate)
    app.run()

if __name__ == "__main__":
    main()

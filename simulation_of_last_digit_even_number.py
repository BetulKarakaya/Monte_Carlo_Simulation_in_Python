import numpy as np
import matplotlib.pyplot as plt

"""
Monte Carlo Simulation for Estimating the Probability of a Phone Number's Last Digit Being Even.

This script generates random phone numbers according to the North American Numbering Plan (NANP) 
and performs a Monte Carlo simulation to determine the probability that the last digit is even. 

Key Features:
- Generates phone numbers with valid first-digit constraints (2-9).
- Uses a large number of samples for statistical accuracy.
- Computes and visualizes the probability distribution.
- Displays histogram and pie chart with additional text explanations.
"""

class PhoneNumber:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        self.probability = 0
        np.random.seed(100)  # Ensure reproducibility

    def monte_carlo_even_num_last_digit(self):
        """In the American telephone numbering system, a phone number cannot start with 0 or 1. 
        Therefore, we generated the first digit separately."""
        first_digit = np.random.randint(low=2, high=10, size=(self.num_samples, 1))
        other_digits = np.random.randint(low=0, high=10, size=(self.num_samples, 9))

        self.all_phone_numbers = np.hstack((first_digit, other_digits))
        self.last_digits = self.all_phone_numbers[:, -1]  
        self.even_last_digits = np.sum(self.last_digits % 2 == 0)

        self.probability = self.even_last_digits / self.num_samples

    def display_results(self):
        theoretical_probability = 5 / 10  # 5 even numbers out of 10 (0,2,4,6,8)
        error_margin = abs(theoretical_probability - self.probability)

        print("\nMonte Carlo Simulation Results:")
        print(f"Total Sample Size: {self.num_samples}")
        print(f"Estimated Probability (Last Digit Even): {self.probability:.4f}")
        print(f"Theoretical Probability: {theoretical_probability:.4f}")
        print(f"Error Margin: {error_margin:.6f}")

    def visualization(self):
        colors = ["#81a4f7", "#a8f781"]
        labels = ["Even Number", "Odd Number"]

        fig, axes = plt.subplots(1, 2, figsize=(15, 8))

        axes[0].hist(self.last_digits, bins=10, color=colors[0], edgecolor="black")
        axes[0].set_title("Distribution of Last Digits of Phone Numbers", fontsize=14,  color = "#393d47")
        axes[0].set_xlabel("Last Digit")
        axes[0].set_ylabel("Frequency")

        axes[1].pie(
            [self.probability, 1 - self.probability],
            colors=colors,
            labels=labels,
            autopct="%1.2f%%",
            textprops={'color':"#393d47", 'fontsize': 13},
            startangle=90
        )
        axes[1].set_title("Probability Distribution of the Last Digit Being Odd or Even", fontsize=14,  color = "#393d47")
        
        fig.suptitle(
            "Monte Carlo Simulation: Probability of Phone Number Ending in an Even Number",
            fontsize=17,  color = "#393d47", weight="bold"
        )

        line = plt.Line2D((.5, .5), (.15, .9), linestyle="--", linewidth=2, color="grey")
        fig.add_artist(line)

        fig.text(
            0.5, 0.05,
            f"Theoretical Probability: 50% | Estimated Probability: {self.probability:.2%} | Error Margin: {abs(0.5 - self.probability):.6f}",
            ha="center", fontsize=12, color="#555555"
        )

        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):
        self.monte_carlo_even_num_last_digit()
        self.display_results()
        self.visualization()

def main():
    
    try:
        num_samples = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_samples < 100000:
            num_samples = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except ValueError:
        num_samples = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")

    app = PhoneNumber(num_samples=num_samples)
    app.run()

if __name__ == "__main__":
    main()

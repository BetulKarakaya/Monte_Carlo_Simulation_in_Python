import numpy as np
import matplotlib.pyplot as plt

"""
    A class to perform a Monte Carlo simulation to estimate the probability of a specific digit 
    appearing a given number of times in randomly generated phone numbers.
"""
class PhoneNumber:
    def __init__(self, num_samples, searched_num=2, rep_num=2):
        """
        Initializes the simulation parameters.

        Parameters:
        num_samples (int): Number of phone numbers to generate.
        searched_num (int): The digit to search for in each generated phone number.
        rep_num (int): The number of times the searched digit should appear.
        """
        self.num_samples = num_samples
        self.searched_num = searched_num
        self.rep_num = rep_num
        self.probability = 0
        np.random.seed(100)  

    def monte_carlo_simulation(self):
    
        """
        In the American telephone numbering system, a phone number cannot start with 0 or 1. 
        Therefore, we generated the first digit separately.
        """
        first_digit = np.random.randint(low=2, high=10, size=(self.num_samples, 1))
        other_digits = np.random.randint(low=0, high=10, size=(self.num_samples, 9))

        self.all_phone_numbers = np.hstack((first_digit, other_digits))
        self.all_rows_search_num = np.sum(self.all_phone_numbers == self.searched_num, axis=1)
        self.all_rows_rep = np.sum(self.all_rows_search_num == self.rep_num)

        self.probability = self.all_rows_rep / self.num_samples

    def display_results(self):
        self.theoretical_probability = pow(1 / 9, self.rep_num)
        self.error_margin = abs(self.theoretical_probability - self.probability)

        print("\nMonte Carlo Simulation Results:")
        print(f"Total Sample Size: {self.num_samples}")
        print(f"Estimated Probability: {self.probability:.6f}")
        print(f"Theoretical Probability: {self.theoretical_probability:.6f}")
        print(f"Error Margin: {self.error_margin:.6f}")

    def visualization(self):
        colors = ["#81a4f7", "#a8f781"]
        labels = [f"Probability of {self.searched_num} repeating {self.rep_num} times", "Probability of not happening"]

        fig, axes = plt.subplots(1, 2, figsize=(15, 8))

        axes[0].bar(labels, [self.all_rows_rep, self.num_samples - self.all_rows_rep], color=colors[0])
        axes[0].set_title(f"Probability of {self.searched_num} appearing {self.rep_num} times", fontsize=14, color="#393d47")
        axes[0].grid()
        axes[0].set_axisbelow(True)

        axes[1].pie(
            [self.probability, 1 - self.probability],
            colors=colors,
            labels=labels,
            autopct="%1.2f%%",
            textprops={'color': "#393d47", 'fontsize': 13},
            startangle=90
        )
        axes[1].set_title("Probability Distribution", fontsize=14, color="#393d47")

        fig.suptitle(
            "Monte Carlo Simulation: Probability of Number Repetition",
            fontsize=17, color="#393d47", weight="bold"
        )

        fig.text(
            0.5, 0.05,
            f"Theoretical Probability: {self.theoretical_probability:.6f} | Estimated Probability: {self.probability:.6%} | Error Margin: {self.error_margin:.6f}",
            ha="center", fontsize=12, color="#555555"
        )

        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):
        self.monte_carlo_simulation()
        self.display_results()
        self.visualization()

def main():
    try:
        num_samples = int(input("Enter the number of samples (≥ 100,000 recommended): "))
        if num_samples < 100000:
            print("Warning: Sample size adjusted to 100,000.")
            num_samples = 100000
    except ValueError:
        print("Invalid input. Defaulting sample size to 100,000.")
        num_samples = 100000

    try:
        searched_num = int(input("Enter the number to search for (0-9): "))
        if not (0 <= searched_num <= 9):
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting searched number to 2.")
        searched_num = 2

    try:
        rep_num = int(input(f"Enter how many times {searched_num} should appear: "))
        if rep_num < 1:
            raise ValueError
    except ValueError:
        print("Invalid input. Defaulting repetition number to 2.")
        rep_num = 2

    app = PhoneNumber(num_samples=num_samples, searched_num=searched_num, rep_num=rep_num)
    app.run()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
📌 Monte Carlo Simulation: Probability of Passing a Multiple-Choice Test with Random Answers

🔹 This simulation estimates the probability of passing a multiple-choice test by randomly guessing answers.
🔹 The test consists of a given number of questions, each with four answer choices (A, B, C, D).
🔹 A large number of simulated tests (e.g., 100,000) are generated to analyze the probability distribution.
🔹 The code calculates:
    - The number of correct answers in each test.
    - The percentage score for each test.
    - The probability of scoring above the passing grade.
🔹 The results are visualized using:
    - A histogram of success rates.
    - A score distribution chart with passing and average score indicators.
🔹 The simulation demonstrates the concept of probability and expected success rates when answering randomly.

🎯 Expected Outcome:
- The probability of passing the test should be very low for large test sizes.
- The average score should converge to 25% of the total possible score (since each answer has a 1/4 chance of being correct).
"""

class TestScore:

    def __init__(self, question_count = 20, passing_grade = 50, num_experiments = 100000):
        np.random.seed(100)
        self.question_count = question_count
        self.passing_grade = passing_grade
        self.num_experiments = num_experiments
        self.answer_key = np.random.choice(["A","B","C","D"], size = self.question_count)
        self.probability = 0

    def monte_carlo_passing_test(self):
        experiments = []
        for _ in range(self.num_experiments):
            all_answers = np.random.choice(["A","B","C","D"], size = self.question_count)
            correct_answer = 0
            for i, answer in enumerate(all_answers):
                if answer == self.answer_key[i]:
                    correct_answer += 1  
    
            experiments.append([correct_answer, correct_answer * (100 / self.question_count), correct_answer/ self.question_count])

        self.df = pd.DataFrame(experiments, columns= ["Correct Answers", "Score", "Success Rate"])
        self.all_passed = len(self.df[self.df["Score"] > 50])
        self.probability =  self.all_passed / self.num_experiments

    def display_result(self):
        print(f"Out Of {self.num_experiments} random test, only {self.all_passed} is higger than or equal passing score")
        print(f"Maximum true guess in a test is {self.df['Correct Answers'].max()}")
        print(f"Minumum true guess in a test is {self.df['Correct Answers'].min()}")
        print(f"Average true guess in a test is {self.df['Correct Answers'].mean()}")
        print(f"Probability of passing test with random answers is {self.probability}")

    def visualization(self):
        
        fig, axes = plt.subplots(1,2,figsize = (16,8))
        
        axes[0].hist(self.df["Success Rate"], label = "Success Rate Distrubition", color = "#81a4f7", edgecolor = "#6281cc", linewidth = .7)
        axes[0].set_xlim(0, 1)
        axes[0].axvline(self.df["Success Rate"].mean(), linewidth = 3, linestyle ="--", color = "#faca9b", label = "Average Success Rate")
        axes[0].grid()
        axes[0].set_axisbelow(True)
        axes[0].legend()
        
        axes[1].hist(self.df["Score"], label = "Score Distrubition", color = "#79e630", edgecolor = "#75c73e", linewidth = .7)
        axes[1].axvline(self.passing_grade, linewidth = 3, linestyle ="--", color = "#3e75c7", label = "Passing Score")
        axes[1].axvline(self.df["Score"].mean(), linewidth = 3, linestyle = "-.", color = "#703ec7", label = "Average Score")
        axes[1].legend()
        fig.text(
            0.5,
            0.02,
            f"Out Of {self.num_experiments} random test, only {self.all_passed} is higger than or equal passing score\n"
            f"Maximum true guess in a test is {self.df['Correct Answers'].max()} and score is = {self.df['Score'].max()}\n"
            f"Minumum true guess in a test is {self.df['Correct Answers'].min()} and score is = {self.df['Score'].min()}\n"
            f"Average true guess in a test is {self.df['Correct Answers'].mean()} and score is = {self.df['Score'].mean()}\n"
            f"Probability of passing test with random answers is {self.probability}\n",
            ha="center", va="bottom", fontsize=14, color="#393d47"
        )
        fig.suptitle("Monte Carlo Simulation: Passing Test With Random Answers", fontsize=18, color="#393d47", weight = "bold")
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.3, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):

        self.monte_carlo_passing_test()
        self.display_result()
        self.visualization()

def main():

    try:
        question_count = int(input("Please enter the number of questions in the test: "))
    except:
        question_count = 20
        print("Warning: A non-numeric input was detected, so the number of questions has been set to 20.")

    try:
        passing_grade = int(input("Please enter the passing grade (0-100): "))
        if not (0 <= passing_grade <= 100):
            passing_grade = 50
            print("Warning: The passing grade must be between 0 and 100. It has been set to 50.")
    except:
        passing_grade = 50
        print("Warning: A non-numeric input was detected, so the passing grade has been set to 50.")

    try:
        num_experiment = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_experiment < 100000:
            num_experiment = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_experiment = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")

    app = TestScore(question_count=question_count, passing_grade=passing_grade, num_experiments=num_experiment)
    app.run()

if __name__ == "__main__":

    main()
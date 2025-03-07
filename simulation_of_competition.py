import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.gridspec as gridspec

"""
Monte Carlo Simulation: Probability of Being Selected in a Competition and Answering the Question Correctly.

This simulation estimates the probability of a contestant being randomly selected in a competition
and the probability of them correctly answering a question. The competition consists of a given number 
of contestants, and each question has multiple-choice options.

Key Features:
- Simulates a competition where participants are chosen randomly.
- Computes the probability of selection and of knowing the answer.
- Visualizes results using bar charts and a heatmap.

"""

class Competition:
    def __init__(self, size=100000, num_contestants=20, num_question_option=4): 
        self.size = size
        self.num_contestants = num_contestants
        self.num_question_option = num_question_option

    def monte_carlo_competition(self):
       
        np.random.seed(100)
        self.all_chosen_contestants = np.random.choice(self.num_contestants, size=self.size)

        self.df = (pd.DataFrame(self.all_chosen_contestants)
                   .value_counts()
                   .reset_index()
                   .rename(columns={0: "Contestant", "count": "Count"})
                   .sort_values(by="Contestant", ignore_index=True)
                   )

        self.df["Probability_Being_Selected"] = self.df["Count"] / self.size
        self.df["Probability_Knowing_Question"] = self.df["Probability_Being_Selected"] * (1 / self.num_question_option)

    def display_results(self):
        
        most_selected = self.df.iloc[self.df["Count"].idxmax()]
        least_selected = self.df.iloc[self.df["Count"].idxmin()]

        print("\n📌 Simulation Results:")
        print(f"Total Simulations: {self.size}")
        print(f"Number of Contestants: {self.num_contestants}")
        print(f"Number of Answer Choices per Question: {self.num_question_option}\n")
        
        print(f"🔹 Highest Selection Probability: Contestant {most_selected['Contestant']} - {most_selected['Probability_Being_Selected']:.4f}")
        print(f"🔹 Lowest Selection Probability: Contestant {least_selected['Contestant']} - {least_selected['Probability_Being_Selected']:.4f}")
        print(f"🎯 Probability of a Selected Contestant Knowing the Answer: {self.df['Probability_Knowing_Question'].mean():.4f}")

    def visualization(self):

        colors = ["#81a4f7", "#a8f781", "#b081f7", "#faa946"]
        gradient = ["#81a4f7", "#8193f7", "#8381f7", "#9d81f7", "#7457b3"]


        fig = plt.figure(figsize=(16.5, 9.5))
        gs = gridspec.GridSpec(1, 2, width_ratios=[5, 3])
        gs_left = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[0])

        axes_0 = plt.subplot(gs_left[0])
        axes_0.bar(self.df["Contestant"], self.df["Probability_Being_Selected"], color=colors[0])
        axes_0.set_xticks(np.arange(0, self.num_contestants,1))
        axes_0.grid()
        axes_0.set_axisbelow(True)
        axes_0.set_title("Distribution of Probability of Selection of Contestants", fontsize=14, color="#393d47")

        axes_1 = plt.subplot(gs_left[1])
        axes_1.bar(self.df["Contestant"], self.df["Probability_Knowing_Question"], color=colors[1])
        axes_1.set_xticks(np.arange(0, self.num_contestants,1))
        axes_1.grid()
        axes_1.set_axisbelow(True)
        axes_1.set_title("Probability of Being Selected and Answering Correctly", fontsize=14, color="#393d47")

        # Heatmap for frequency distribution
        axes_2 = plt.subplot(gs[1])
        sn.heatmap(
            self.df[["Count"]],
            cmap=sn.color_palette(gradient, len(gradient)),
            annot=True,
            annot_kws={"size": 14, "color": "w"},
            fmt=".2f",
            linewidths=0.5,
            linecolor="black",
            ax=axes_2
        )
        axes_2.set_ylabel("Contestants", fontsize=14, color="#393d47")
        axes_2.set_xlabel("Frequency", fontsize=14, color="#393d47")
        axes_2.set_title("Frequency Distribution Heatmap", fontsize=14, color="#393d47")

        line = plt.Line2D((.6, .6), (.1, .92), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line)
        line2 = plt.Line2D((.05, .52), (0.5, 0.5), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line2)

        
        fig.suptitle("Monte Carlo Simulation: Probability of Being Selected in the Competition and Answering the Question Correctly", fontsize=17, color="#393d47", weight="bold")
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.85, wspace=0.4, hspace=0.4)
        plt.show()

    def run(self):
        self.monte_carlo_competition()
        self.display_results()
        self.visualization()


def main():

    try:
        size = int(input("Enter the number of simulations (default: 100,000): "))
        if size < 100000:
            size = 100000
            print("⚠️ Warning: Input too low. Defaulting to 100,000 simulations.")
    except:
        size = 100000
        print("⚠️ Warning: Invalid input detected. Defaulting to 100,000 simulations.")

    try:
        num_contestants = int(input("Enter the number of contestants (default: 20): "))
        if num_contestants < 2:
            num_contestants = 20
            print("⚠️ Warning: Contestants must be at least 2. Defaulting to 20.")
    except:
        num_contestants = 20
        print("⚠️ Warning: Invalid input detected. Defaulting to 20 contestants.")

    try:
        num_question_option = int(input("Enter the number of answer choices (default: 4): "))
        if num_question_option < 2:
            num_question_option = 4
            print("⚠️ Warning: Must be at least 2 answer choices. Defaulting to 4.")
    except:
        num_question_option = 4
        print("⚠️ Warning: Invalid input detected. Defaulting to 4 answer choices.")

    app = Competition(size=size, num_contestants=num_contestants, num_question_option=num_question_option)
    app.run()


if __name__ == "__main__":
    main()

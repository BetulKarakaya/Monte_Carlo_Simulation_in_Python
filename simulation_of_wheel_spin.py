import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import seaborn as sn

class Wheel_EqualDivide:
    def __init__(self, num_spin=100000, section_size=8):
        """
        Initialize the simulation with the number of spins and section size.
        
        :param num_spin: Number of wheel spins (default is 100,000)
        :param section_size: Number of sections on the wheel (default is 8)
        """
        self.num_spin = num_spin
        self.section_size = section_size

    def monte_carlo_wheel(self):
        """
        Simulate the wheel spins and compute the frequency of each section.
        Also, calculates the probability for each section based on its frequency.
        """
        np.random.seed(100)
        self.all_spins = np.random.randint(low=1, high=self.section_size + 1, size=self.num_spin)
        
        self.df = (pd.DataFrame(self.all_spins)
                   .value_counts()
                   .reset_index()
                   .rename(columns={0: "Chosen Section", "count": "Frequency"})
                   .sort_values(by="Chosen Section", ignore_index=True)
                  )

        # Calculate probability for each section
        self.df["Probability"] = self.df["Frequency"] / self.num_spin

    def display_results(self):
        """
        Display the results of the Monte Carlo simulation, including the chosen section and its frequency.
        This is a detailed output of the outcome of the simulation.
        """
        print("Results of the Monte Carlo Simulation:")
        print(f"Total Spins: {self.num_spin}")
        print(f"Total Sections: {self.section_size}")
        print("\nDistribution of Outcomes (Section, Frequency, Probability):\n")
        
        for index, row in self.df.iterrows():
            print(f"Section: {row['Chosen Section']} | Frequency: {row['Frequency']} | Probability: {row['Probability']:.4f}")

    def visualization(self):
        """
        Visualize the results of the simulation through a pie chart, bar graph, and heatmap.
        The pie chart shows the probability distribution, the bar chart shows the frequency of outcomes,
        and the heatmap visualizes the frequency distribution.
        """
        colors = ["#81a4f7", "#a8f781", "#b081f7", "#faa946"]
        gradient = ["#81a4f7", "#8193f7", "#8381f7", "#9d81f7", "#7457b3"]
        
        # Create a figure with subplots
        fig = plt.figure(figsize=(16.5, 9.5))
        gs = gridspec.GridSpec(1, 2, width_ratios=[5, 3])
        gs_left = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[0])
    
        # Pie chart showing the probability distribution
        axes_0 = plt.subplot(gs_left[0])
        axes_0.pie(
            self.df["Probability"], 
            labels=self.df["Chosen Section"], 
            colors=colors, 
            autopct="%1.2f%%",
            startangle=90,
            textprops={'color': "#393d47", 'fontsize': 12}
        )
        axes_0.set_title("Chance of Landing on Each Section", fontsize=14, color="#393d47")
        
        # Bar chart showing the frequency distribution
        axes_1 = plt.subplot(gs_left[1])
        axes_1.bar(self.df["Chosen Section"], self.df["Frequency"], color=colors[0])
        axes_1.grid()
        axes_1.set_axisbelow(True)
        axes_1.set_title("Distribution of Wheel Spin Outcomes", fontsize=14, color="#393d47")
        
        # Heatmap for frequency distribution
        axes_2 = plt.subplot(gs[1])
        axes_2 = sn.heatmap(
            self.df[["Frequency"]],
            cmap=sn.color_palette(gradient, len(gradient)),
            annot=True,
            annot_kws={"size": 14, "color": "w"},
            fmt=".2f", 
            linewidths=0.5, 
            linecolor="black"
        )
        axes_2.set_ylabel("Section", fontsize=14, color="#393d47")
        axes_2.set_xlabel("Frequency", fontsize=14, color="#393d47")
        axes_2.set_title("Frequency Distribution Heatmap", fontsize=14, color="#393d47")
        
        # Add dividing lines for better layout
        line = plt.Line2D((.55, .55), (.1, .92), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line)
        
        line2 = plt.Line2D((.05, .52), (0.5, 0.5), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line2)
        
        # Main title for the figure
        fig.suptitle("Monte Carlo Simulation: Probability Analysis of an Equally Divided Wheel", fontsize=17, color="#393d47", weight="bold")
        
        # Adjust layout and show the figure
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.85, wspace=0.4, hspace=0.4)
        plt.show()

    def run(self):
        
        self.monte_carlo_wheel()
        self.display_results()
        self.visualization()

def main():
    
    try:
        num_spin = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if num_spin < 100000:
            num_spin = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        num_spin = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")
    
    try:
        section_size = int(input("Enter the number of sections for the wheel (e.g., 8, 10, 12): "))
        if section_size < 1:
            section_size = 8
            print("Warning: The number of sections must be positive. Defaulting to 8 sections.")
    except:
        section_size = 8
        print("Warning: Invalid input detected, defaulting to 8 sections.")
    
    app = Wheel_EqualDivide(num_spin=num_spin, section_size=section_size)
    app.run()

if __name__ == "__main__":
    main()

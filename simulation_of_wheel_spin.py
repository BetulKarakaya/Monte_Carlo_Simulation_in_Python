import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import seaborn as sn


class Wheel_EqualDivide:
    def __init__(self, num_spin = 100000, section_size = 8):
        
        self.num_spin = num_spin
        self.section_size = section_size

    def monte_carlo_wheel(self):
        np.random.seed(100)
        self.all_spins = np.random.randint(low = 1, high = self.section_size +1, size = self.num_spin)
        self.df = (pd.DataFrame(self.all_spins)
        .value_counts()
        .reset_index()
        .rename(columns = {0: "Chosen Section", "count": "Frequency"})
        .sort_values(by= "Chosen Section", ignore_index = True)
        )

        self.df["Probability"] = self.df["Frequency"] / self.num_spin
        print(self.df)

    def display_results(self):
        pass

    def visualization(self):
        
        colors = ["#81a4f7", "#a8f781", "#b081f7", "#faa946"]
        gradient = ["#81a4f7", "#8193f7","#8381f7", "#9d81f7","#7457b3"]
        fig = plt.figure(figsize=(16.5, 9.5))
        
        gs = gridspec.GridSpec(1, 2, width_ratios=[5, 3])  
        gs_left = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[0])
    
        axes_0 = plt.subplot(gs_left[0])
        axes_0.pie(
            self.df["Probability"], 
            labels = self.df["Chosen Section"], 
            colors = colors, 
            autopct = "%1.2f%%",
            startangle=90,
            textprops={'color': "#393d47", 'fontsize': 12}
            )
        axes_0.set_title("Chance of Landing on Each Section", fontsize=14, color="#393d47")
        
        axes_1 = plt.subplot(gs_left[1])
        axes_1.bar(self.df["Chosen Section"], self.df["Frequency"], color = colors[0])
        axes_1.grid()
        axes_1.set_axisbelow(True)
        axes_1.set_title("Distribution of Wheel Spin Outcomes", fontsize=14, color="#393d47")
        
        axes_2 = plt.subplot(gs[1])
        axes_2 = sn.heatmap(
            self.df[["Frequency"]],
            cmap= sn.color_palette(gradient, len(gradient)),
            annot=True,
            annot_kws={"size": 14,"color": "w"},
            fmt=".2f", 
            linewidths=0.5, 
            linecolor="black",
            )
        axes_2.set_ylabel("Section", fontsize=14, color="#393d47")
        axes_2.set_xlabel("Frequency", fontsize=14, color="#393d47")
        axes_2.set_title("Frequency Distribution Heatmap",fontsize=14, color="#393d47")
        
        line = plt.Line2D((.55, .55), (.1, .92), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line)
        
        line2 = plt.Line2D((.05, .52),(0.5, 0.5), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line2)
        
        fig.suptitle("Monte Carlo Simulation: Probability Analysis of an Equally Divided Wheel", fontsize=17, color= "#393d47", weight = "bold")
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.85, wspace=0.4, hspace=0.4)
        plt.show()
        
       

    def run(self):
        self.monte_carlo_wheel()
        self.display_results()
        self.visualization()


def main():

    app = Wheel_EqualDivide()
    app.run()


if __name__ == "__main__":
    main()
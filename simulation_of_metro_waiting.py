import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

"""
🚇 Monte Carlo Simulation: Metro Station Waiting Time 🚇

This simulation estimates the probability that two people arriving 
randomly between 0 and 10 minutes at a metro station will NOT meet, 
i.e., the time difference between them exceeds 5 minutes.

Key Features:
- Simulates random arrival times for two people.
- Calculates how often the absolute time difference exceeds 5 minutes.
- Visualizes arrival time pairs and highlights the meeting region.
- Estimates the probability of not meeting (|A - B| > 5).
- Computes error margin to understand statistical uncertainty.

🎯 Expected Outcome:
- Theoretically, the probability that two people do *not* meet 
  (|A - B| > 5) is 25%.
"""

class MetroWaitSim:
    def __init__(self, num_samples=100000):
        self.num_samples = max(num_samples, 100000)  # at least 100,000
        self.seed = 100
        np.random.seed(self.seed)

    def simulate(self):
        self.arrival_a = np.random.uniform(0, 10, self.num_samples)
        self.arrival_b = np.random.uniform(0, 10, self.num_samples)

        time_diff = np.abs(self.arrival_a - self.arrival_b)
        self.not_meeting = time_diff > 5
        self.not_meet_prob = np.mean(self.not_meeting)

        self.calculate_error_margin()

    def calculate_error_margin(self, confidence=0.95):
        z = 1.96 if confidence == 0.95 else 1.64
        p = self.not_meet_prob
        n = self.num_samples
        self.error_margin = z * np.sqrt((p * (1 - p)) / n)

    def display_result(self):
        print("\n🚇 Monte Carlo Simulation: Metro Station Meeting Probability 🚇")
        print(f"Total Simulations: {self.num_samples}")
        print(f"\n❌ Probability that they do NOT meet (|A - B| > 5 min): {self.not_meet_prob:.4f}")
        print(f"📏 Error Margin (95% confidence): ±{self.error_margin:.4f}")
        print("\n📌 Note: As the number of samples increases, the result should converge to the theoretical value (≈ 0.25).")

    def visualize(self):
        fig, ax = plt.subplots(figsize=(12,8))
        ax.scatter(self.arrival_a, self.arrival_b, 
                   c=np.where(self.not_meeting, "red", "green"), 
                   alpha=0.3, s=1)

        x = np.linspace(0, 10, 1000)
        y1 = x - 5  # B = A - 5
        y2 = x + 5  # B = A + 5

        ax.plot(x, y1, "k--", lw=1.5)
        ax.plot(x, y2, "k--", lw=1.5)

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        ax.set_xlabel("Arrival Time of Person A (min)", fontsize=12)
        ax.set_ylabel("Arrival Time of Person B (min)", fontsize=12)

        green_patch = mpatches.Patch(color="#a8f781", label="They meet (≤ 5 min)")
        red_patch = mpatches.Patch(color="#ff9999", label="Do not meet (> 5 min)")
        border_line = mlines.Line2D([], [], color="black", linestyle="--", linewidth=1.5, label="|A - B| = 5")

        ax.legend(handles=[green_patch, red_patch, border_line], loc="upper left", frameon=True, facecolor="white", edgecolor="gray")

        fig.suptitle(
            "Monte Carlo Simulation: Probability of Metro Station Waiting Time",
            fontsize=17, color="#393d47", weight="bold"
        )

        fig.text(
            0.5, 0.05,
            f"Theoretical Probability: ≈ 0.25 | Estimated Probability: {self.not_meet_prob:.6%} | Error Margin: {self.error_margin:.6f}",
            ha="center", fontsize=12, color="#555555"
        )
        plt.grid(True)
        plt.gca().set_axisbelow(True)
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

    def run(self):
        self.simulate()
        self.display_result()
        self.visualize()


def main():
    try:
        user_input = int(input("Please enter number of simulations (minimum 100,000): "))
        if user_input < 100000:
            print("⚠️ Input adjusted to 100,000 for better accuracy.")
            user_input = 100000
    except:
        print("⚠️ Invalid input detected. Defaulting to 100,000 simulations.")
        user_input = 100000

    app = MetroWaitSim(user_input)
    app.run()


if __name__ == "__main__":
    main()

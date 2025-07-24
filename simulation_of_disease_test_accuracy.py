import matplotlib.pyplot as plt
import random


class MonteCarloAccuracyDisease:

    def __init__(self, population_size=10000, disease_rate=0.01, true_positive_rate=0.95, false_positive_rate=0.05):
        self.population_size = population_size
        self.disease_rate = disease_rate
        self.true_positive_rate = true_positive_rate
        self.false_positive_rate = false_positive_rate

        self.false_negative_rate = 1 - self.true_positive_rate 
        self.true_negative_rate = 1 - self.false_positive_rate 

        self.true_positives = 0
        self.false_positives = 0
        self.true_negatives = 0
        self.false_negatives = 0

        self.healthy_population_size = 0
        self.diseased_population_size = 0

        self.positives_test = 0
        self.negatives_test = 0

    def monte_carlo_accuracy_simulation(self):
        for _ in range(self.population_size):
            if random.uniform(0, 1) < self.disease_rate:
                self.diseased_population_size += 1

                if random.uniform(0, 1) < self.true_positive_rate:
                    self.true_positives += 1
                else:
                    self.false_negatives += 1
            else:
                self.healthy_population_size += 1

                if random.uniform(0, 1) < self.false_positive_rate:
                    self.false_positives += 1
                else:
                    self.true_negatives += 1

        self.positives_test = self.true_positives + self.false_positives
        self.negatives_test = self.true_negatives + self.false_negatives

    def display_results(self):
        print("\n🔬 Monte Carlo Simulation Results on Disease Testing Device Accuracy 🔬")
        print(f"Population Size: {self.population_size}")
        print(f"True Positives: {self.true_positives}")
        print(f"False Positives: {self.false_positives}")
        print(f"True Negatives: {self.true_negatives}")
        print(f"False Negatives: {self.false_negatives}\n")

        print("🎯 Precision (Proportion of positive results that are actually sick)")
        precision = self.true_positives / (self.true_positives + self.false_positives)
        print(f"Precision = TP / (TP + FP): {precision:.4f}")

        print("\n💉 Sensitivity / Recall (Proportion of actual sick people caught by the test)")
        sensitivity = self.true_positives / (self.true_positives + self.false_negatives)
        print(f"Sensitivity = TP / (TP + FN): {sensitivity:.4f}")

    def visualization(self):
        colors = ["#81a4f7", "#a8f781", "#ffa81c", "#fc5252"]
        labels = ["True Positives", "False Positives", "True Negatives", "False Negatives"]
        sizes = [self.true_positives, self.false_positives, self.true_negatives, self.false_negatives]
        explode = [0.1, 0.1, 0.1, 0]

        fig, ax = plt.subplots(figsize=(10,10))
        ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",
               textprops={'color': "#393d47", 'fontsize': 13}, startangle=45,explode=explode,wedgeprops={'edgecolor': 'white', 'linewidth': 2},radius=1.3)

        ax.set_title("Diagnostic Accuracy Breakdown", color="#393d47", fontsize=15)
        fig.suptitle("Monte Carlo Simulation: Diagnostic Performance of Disease Test Device",
                     fontsize=17, color="#393d47", weight="bold")
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()


def main():
    print("\n💡 Welcome to the Disease Diagnosis Simulation using Monte Carlo Method 💡\n")

    try:
        population_size = int(input("Please enter population size for the simulation (e.g., 10,000): "))
        if population_size < 1000:
            population_size = 10000
            print("⚠️ Population size too small. Automatically adjusted to 10,000.")
    except:
        population_size = 10000
        print("⚠️ Invalid input. Default population size set to 10,000.")

    try:
        disease_rate = float(input("Enter disease prevalence rate (e.g., 0.01 for 1%): "))
        if not 0 < disease_rate < 1:
            disease_rate = 0.01
            print("⚠️ Invalid range. Default disease rate of 1% applied.")
    except:
        disease_rate = 0.01
        print("⚠️ Invalid input. Default disease rate of 1% applied.")

    try:
        tpr = float(input("Enter True Positive Rate (e.g., 0.95): "))
        fpr = float(input("Enter False Positive Rate (e.g., 0.05): "))
        if not (0 <= tpr <= 1) or not (0 <= fpr <= 1):
            raise ValueError
    except:
        tpr = 0.95
        fpr = 0.05
        print("⚠️ Invalid input. Default rates applied: TPR = 0.95, FPR = 0.05")

    print("\n⏳ Running simulation... Please wait.\n")

    app = MonteCarloAccuracyDisease(population_size=population_size,
                                    disease_rate=disease_rate,
                                    true_positive_rate=tpr,
                                    false_positive_rate=fpr)

    app.monte_carlo_accuracy_simulation()
    app.display_results()
    app.visualization()


if __name__ == "__main__":
    main()

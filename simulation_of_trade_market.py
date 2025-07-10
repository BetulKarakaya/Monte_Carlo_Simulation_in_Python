import numpy as np
import matplotlib.pyplot as plt

"""
📈 Monte Carlo Trade Market Simulation 📈

Simulates random stock price changes over 30 days using normally distributed daily returns.
Calculates the probability of reaching a profit (take-profit) or a loss (stop-loss) threshold 
before the month ends. Includes visualization of the final outcomes.

Key Features:
- Uses daily returns with Gaussian distribution (mean = 0.05%, std = 1%)
- Simulates 30-day price evolution for each run
- Applies stop-loss and take-profit exit rules
- Calculates probability of profit
- Visualizes outcome distribution

Author: 💕Your Favorite AI Assistant
"""


class MonteCarloTradeMarket:

    def __init__(self, starting_price, take_profit_price, stop_loss_price, rep_num):
        self.starting_price = starting_price
        self.take_profit_price = take_profit_price
        self.stop_loss_price = stop_loss_price
        self.rep_num = rep_num
        self.all_monthly_profit = []
        self.probability = 0

    def monte_carlo_trade(self):
        np.random.seed(100)
        
        for _ in range(self.rep_num):
            price = self.starting_price
            success = None

            for _ in range(30):
                daily_return = np.random.normal(loc=0.0005, scale=0.01)
                price *= (1 + daily_return)

                if price >= self.take_profit_price:
                    success = True  # Take-profit triggered
                    break
                elif price <= self.stop_loss_price:
                    success = False  # Stop-loss triggered
                    break

            # If neither stop-loss nor take-profit was hit after 30 days
            if success is None:
                success = price > self.starting_price

            self.all_monthly_profit.append(success)

        # Calculate probability of making a profit
        self.probability = np.mean(self.all_monthly_profit)

    def display_results(self):
        total_success = sum(self.all_monthly_profit)
        total_failures = self.rep_num - total_success

        print("\n📊 Monte Carlo Trading Simulation Results 📊")
        print(f"Total Simulations      : {self.rep_num}")
        print(f"✅ Profitable Outcomes : {total_success}")
        print(f"❌ Losing Outcomes     : {total_failures}")
        print(f"📈 Probability of Profit: {self.probability:.4f} ({self.probability * 100:.2f}%)")

    def visualization(self):
        # Bar chart of outcomes
        labels = ['Profit', 'Loss']
        counts = [sum(self.all_monthly_profit), self.rep_num - sum(self.all_monthly_profit)]
        colors = ["#f6be06", "#370560"]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(labels, counts, color=colors)

        for i, count in enumerate(counts):
            ax.text(i, count + self.rep_num * 0.01, f"{count}", ha='center', fontsize=12)

        ax.set_title("Monte Carlo Simulation: Trading Outcome Distribution Over One Month", fontsize=17, color="#393d47")
        ax.set_ylabel("Count", fontsize=12)
        ax.set_axisbelow(True)
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.5, hspace=0.4)
        plt.show()

        plt.show()

    def run(self):
        self.monte_carlo_trade()
        self.display_results()
        self.visualization()


def main():
    try:
        rep_num = int(input("🔢 Enter number of simulations (minimum 100,000 recommended): "))
        if rep_num < 100_000:
            print("⚠️ Too low! Setting number of simulations to 100,000.")
            rep_num = 100_000
    except:
        print("⚠️ Invalid input. Using default value: 100,000 simulations.")
        rep_num = 100_000

    app = MonteCarloTradeMarket(
        starting_price=100,
        take_profit_price=110,  # +10%
        stop_loss_price=95,     # -5%
        rep_num=rep_num
    )

    app.run()


if __name__ == "__main__":
    main()

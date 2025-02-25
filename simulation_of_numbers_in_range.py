import matplotlib.pyplot as plt 
import numpy as np

class NumberInRange:

    def __init__(self, space, search, size = 100000):
        
        self.min_space = space["Min"]
        self.max_space = space["Max"]
        self.min_search = search["Min"]
        self.max_search = search["Max"]
        self.size = size
        self.probability = 0

    def monte_carlo_range(self):
        np.random.seed(100)
        self.all_selections = np.random.randint(self.min_space, self.max_space, size= self.size)
        self.all_in_range = sum(1 for x in self.all_selections if self.min_search <= x < self.max_search)
        self.probability = self.all_in_range / self.size

    def display_results(self):

        print(f"Out of {self.size} numbers, {self.all_in_range} is in range of {self.min_search, self.max_search}. The probability of numbers in range of {self.min_search, self.max_search} is {self.probability}.")

    def visualization(self):

        fig, axes = plt.subplots(1,2, figsize = (15,8))
        labels = ["In Range","Out Of Range"]
        colors = ["#81a4f7","#a8f781"]
        values = [self.all_in_range, self.size - self.all_in_range]
        
        axes[0].bar(labels,values, color = colors)
        axes[0].set_yticks(np.arange(0, max(values), self.size/20))
        axes[0].set_title("Distribution of Numbers Inside and Outside the Specified Range", fontsize = 14, color = "#393d47")
        axes[0].grid()
        axes[0].set_axisbelow(True)

        axes[1].pie([self.probability, 1- self.probability], labels = labels, colors = colors, autopct="%1.1f%%", textprops={'color':"#393d47", 'fontsize': 13}, startangle = 90)
        axes[1].set_title("Probability of a Number Appearing in the Specified Range", fontsize = 14, color = "#393d47")
        fig.suptitle("Monte Carlo Simulation: Estimating Probability of Numbers in a Given Range", fontsize = 18, color = "#393d47")

        line = plt.Line2D((.5,.5),(.1,.9), color="#6b6c6e", linewidth=2, linestyle="--")
        fig.add_artist(line)

        # Metni alta yerleştir
        fig.text(
            0.5,  # X konumu (orta)
            0.02,  # Y konumu (en alta yakın)
            f"Out of {self.size} numbers, {self.all_in_range} is in range of [{self.min_search}, {self.max_search}).\n"
            f"The probability of numbers in range [{self.min_search}, {self.max_search}) is {self.probability:.4f}.",
            ha="center", va="bottom", fontsize=14, color="#393d47"
        )

        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.85, wspace=0.2, hspace=0.4)
        plt.show()

    def run(self):

        self.monte_carlo_range()
        self.display_results()
        self.visualization()

def control(space_min, space_max, search_min, search_max):

    if search_min < space_min:
        return False
    if search_max > space_max:
        return False
    if space_max <= space_min:
        return False
    if search_max <= search_min:
        return False
    return True

def main():
    
    try:
        space_min = int(input("Enter the lower limit of the number space: "))  
        space_max = int(input("Enter the upper limit of the number space: "))  

        search_min = int(input("Enter the lower limit of the search range: "))  
        search_max = int(input("Enter the upper limit of the search range: ")) 
        
        if(control(space_min=space_min, space_max=space_max, search_min=search_min, search_max=search_max)):
            search = {"Min": search_min, "Max": search_max}
            space = {"Min": space_min, "Max": space_max}
        else:
            raise ValueError()
    except:
        print("Warning: A non-numeric input was detected, so default space and range have been adjusted to: ")
        print("Space = [0,100)")
        print("Range = [1,10)")

        search = {"Min": 1, "Max": 10}
        space = {"Min": 0, "Max": 100}

    try:
        size = int(input("Please enter a value greater than 100,000 for the simulation sample rate: "))
        if size < 100000:
            size = 100000
            print("Warning: Your input was less than 100,000, so the sample rate has been adjusted to 100,000.")
    except:
        size = 100000
        print("Warning: A non-numeric input was detected, so the sample rate has been adjusted to 100,000.")

    app = NumberInRange(search = search, space = space, size = size)
    app.run()
    
if __name__ == "__main__":
    main()
# 🎲 Monte Carlo Simulations Playground 🎲  

Welcome to the **Monte Carlo Simulations** repository! 🚀 This repo is a collection of Python-based simulations that use the **Monte Carlo method** to estimate probabilities, model real-world scenarios, and analyze randomness. Whether you're a **data scientist, mathematician, or just a curious coder**, this is the perfect place to explore the power of probabilistic simulations.  

---

## 📌 What is Monte Carlo Simulation?  
Monte Carlo simulations rely on **random sampling and statistical modeling** to estimate numerical results that may be difficult (or impossible) to compute analytically. They are widely used in **finance, physics, engineering, AI, and probability theory** to solve problems with uncertainty and randomness.  

### ✅ Key Features of Monte Carlo Simulations:  
✔️ **Random Sampling:** Uses large numbers of random trials  
✔️ **Statistical Approximation:** Estimates probabilities when exact solutions are complex  
✔️ **Real-World Applications:** Used in decision-making, risk analysis, and scientific modeling  

---

## 🚀 Included Simulations  



###  1.🎲[Dice Roll Probability Simulation: Rolling a 6](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_6_on_die.py)

**Goal:** Estimate the probability of rolling a 6 in a large number of dice rolls.

**How It Works:**
- Simulates 100,000 rolls of a fair six-sided die using Monte Carlo methods.
- Counts the number of times a 6 appears.
- Computes the experimental probability of rolling a 6.
- Compares the experimental probability with the theoretical value (1/6 ≈ 16.67%).
- Visualizes the results with:
  - 📊 A bar chart representing the frequency of each die face.
  - 📌 A text summary displaying the probability and count of rolling a 6.
- Demonstrates the Law of Large Numbers, showing how the estimated probability approaches the theoretical probability as the number of trials increases.

### 🎲 2.[Dice Roll Probability Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_dice_roll_distribution.py)
**Goal:** Estimate the probability of rolling a specific sum (e.g., 8) when rolling two six-sided dice.

**How It Works:**
- Simulates 100,000 dice rolls.
- Counts occurrences where the dice sum equals the target.
- Computes the probability and compares it to the theoretical value.
- Visualizes the results with a pie chart. 🥧

### 🪙 3.[Coin Toss Probability Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_coin_toss_distribution.py)
**Goal:** Estimate the probability of getting heads or tails in a large number of coin flips.

**How It Works:**
- Simulates 100,000 coin flips using Monte Carlo methods.
- Calculates the frequency of heads and tails.
- Computes the probability of heads and tails.
- Visualizes the results with:
  - 🥧A pie chart showing the probability distribution of heads and tails.
  - 📊A bar chart displaying the total occurrences of heads and tails.
- Demonstrates the Law of Large Numbers, as the probability should converge to 50% for each outcome when the sample size is large enough.

### 🪙 4.[Three Coin Toss Probability Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_three_coin_toss_distribution.py)
**Goal:** Estimate the probability of getting at least one 'Tails' when flipping three fair coins.

**How It Works:**
- Simulates 100,000 trials where three coins are flipped per trial.
- Determines how many trials contain at least one 'Tails'.
- Computes the estimated probability and compares it to the theoretical probability:

  \[
  P(At least one Tails) = 1 - P(No Tails)
  \]

  \[
  = 1 - (1/2 × 1/2 × 1/2) = 1 - 1/8 = 7/8 ≈ 0.875
  \]

- Visualizes the results with:
  - 📊 A bar chart showing the frequency of 'Heads' and 'Tails' across the three coin flips.
  - 🥧A pie chart illustrating the probability distribution of getting at least one 'Tails'.


 ### 🎲 5.[Dice Face Probability Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_the_sum_of_two_dice.py)
**Goal:** Estimate the probability distribution of each face (1-6) in a large number of dice rolls.

**How It Works:**
- Simulates 100,000 dice rolls using Monte Carlo methods.
- Counts how many times each face (1-6) appears.
- Computes the experimental probability for each face.
- Compares experimental probabilities with the theoretical probability (1/6 ≈ 16.67%).
- Visualization:
   - 📊 Bar Chart: Displays how frequently each face appeared.
   - 🥧 Pie Chart: Shows the probability distribution of each die face.
- 🔢 Demonstrates the Law of Large Numbers, where probabilities should approach 1/6 as the number of trials increases.
This simulation helps understand randomness and probability distribution in rolling a fair die! 🎲✨


### 🎱 6.[Monte Carlo Ball Selection Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/probability_of_ball_selection.py)
**Goal:** Estimate the probability of drawing a specific colored ball from a bag containing multiple colors.  

#### **How It Works:**  
- The user defines the number of **balls for each color** in a bag.  
- A **random ball** is drawn from the bag for a large number of trials (e.g., 100,000).  
- Counts how many times the **target color** is drawn.  
- Computes the experimental probability and compares it with the theoretical probability.  

#### **Visualization:**  
📊 **Bar Chart:** Displays the frequency of each color drawn.  
🥧 **Pie Chart:** Illustrates the probability distribution of the selected ball colors.  

#### **Concepts Demonstrated:**  
🔹 **Law of Large Numbers:** As the number of trials increases, the observed probability should approach the theoretical probability.  
🔹 **Random Sampling:** Simulating real-world probability experiments through random selections.  
🔹 **Monte Carlo Simulation:** Using repeated random sampling to estimate the likelihood of an event.  

This experiment helps understand probability theory in random selection scenarios, like **lotteries, game mechanics, and real-world decision-making processes!** 🎯✨  

### 🔢 7.[Monte Carlo Simulation: Estimating the Probability of Numbers in a Given Range](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_numbers_in_range.py)
**Goal:** Estimate the probability of a randomly selected number falling within a specified range using the Monte Carlo method.

#### How It Works:
- The user defines a number space [min, max) and a search range within this space [min, max).
- A large number (default: 100,000) of random numbers are generated from the space.
- The program calculates how many numbers fall within the search range.
- The probability is computed as the proportion of numbers falling within the specified range.
- Results are displayed as both numerical output and visualized using bar and pie charts.

#### Visualization:
- **Bar Chart:** Displays the distribution of numbers inside and outside the specified range.
- **Pie Chart:** Illustrates the probability of a number appearing within the specified range.
This simulation demonstrates random sampling and probability estimation. It provides insights into understanding randomness and probability theory, which can be applied in fields like data science, statistics, and decision-making.📈📚

 ### 🔢 8.[Monte Carlo Simulation: Estimating the Probability of Even Numbers in a Given Range](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_even_numbers.py)

**Goal**:  
Estimate the probability of randomly selecting an even number from a user-defined range using the Monte Carlo method.  

#### How It Works:  
- The user defines a number space \([ \text{min}, \text{max} )\).  
- A large number (default: 100,000) of random integers are generated within this space.  
- The program calculates how many of these numbers are even.  
- The probability is computed as:  
- **P(even) = Number of even numbers / Total generated numbers**
- Results are displayed both numerically and visually using charts.  

#### **Visualization:** 
- 📊 **Bar Chart**: Displays the distribution of even and odd numbers.  
- 🥧 **Pie Chart**: Illustrates the probability of selecting an even number.  

This simulation demonstrates random sampling and probability estimation. It provides insights into understanding randomness and probability theory, applicable in fields like data science, statistics, and decision-making. 📈📚  

### 🎯 9.[ Monte Carlo Test Passing Probability Simulation](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_passing_test.py) 

#### **Goal:**  
Estimate the probability of passing a multiple-choice test by randomly guessing the answers.

#### **How It Works:**  
- Simulates **100,000** test attempts using Monte Carlo methods.  
- Each test consists of a set number of **multiple-choice questions** (default: 20).  
- Each question has **four answer choices** (A, B, C, D), and the correct answers are randomly assigned.  
- A student **randomly selects answers** for each question.  
- The number of **correct answers, score percentage, and pass rate** are recorded for each test.  
- The simulation calculates the probability of passing based on a **user-defined passing grade** (default: 50%).

#### **Visualization:**  
📊 **Histogram:** Displays the distribution of success rates across all tests.  
📊 **Score Distribution Chart:** Shows how many tests passed and failed, with passing grade and average score indicators.  

#### **Expected Results:**  
- The **probability of passing** should be **low** since random guessing has only a **25% chance per question**.  
- The **average score** should converge to **25% of the total possible score** (since 1 in 4 answers is correct).  
- The **Law of Large Numbers** is demonstrated as the results stabilize with increasing test simulations.  

This simulation provides insights into **random probability, test success rates, and statistical distributions** when guessing blindly on a multiple-choice test! 🎓📖  


### 🎲 10.[Monte Carlo Simulation: Highest of 3 Dice Being 5 or 6](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_three_dice_max.py)
#### **Goal:** 
Estimate the probability that the highest value among three rolled dice is either 5 or 6.

#### **How It Works:**

- Simulates rolling three six-sided dice for a large number of trials (default: 100,000).
- Records the highest value in each roll.
- Counts the occurrences where the highest roll is either 5 or 6.
- Calculates the probability using Monte Carlo methods.
#### **Visualization:**

- 📊 Bar Chart: Displays the count of trials where the highest roll was 5 or 6 versus other outcomes.
- 🥧 Pie Chart: Illustrates the probability distribution of achieving a maximum roll of 5 or 6.

This simulation demonstrates probability principles and the distribution of maximum values in random dice rolls. 🎲✨

### 🏀 11. [Monte Carlo Simulation: Probability of Making at Least 7 Successful Free Throws](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_free_throw_success.py)
#### **Goal:**
Estimate the probability that a basketball player makes at least 7 successful free throws out of 10 attempts.

#### **How It Works:**
- Simulates a large number of free throw attempts (default: 100,000).
- Each free throw has a predefined success rate (default: 80%).
- The simulation calculates how many times the player makes at least 7 successful throws out of 10.
- The probability of making at least 7 successful throws is estimated using Monte Carlo methods.
#### **Visualization:**
- 📊 Bar Chart: Displays the distribution of successful free throws out of 10 attempts.
- 🥧 Pie Chart: Illustrates the probability of making at least 7 successful free throws versus making fewer than 7.

#### **Detailed Results:**
The program prints the number of trials where at least 7 successful free throws were made.
It calculates the estimated probability of achieving this outcome.
It also displays the most common and least common number of successful free throws in the trials.
This simulation showcases how Monte Carlo methods can be used to estimate probabilities in a real-world scenario. 🎯

### 🎡 12. [Monte Carlo Simulation: Probability Analysis of an Equally Divided Wheel](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_wheel_spin.py)
**Goal:**
Estimate the probability of landing on each section of a wheel that is equally divided into a set number of sections, using Monte Carlo simulation.

#### **How It Works:**
-Simulates a large number of spins on an equally divided wheel (default: 100,000 spins).
- Each spin randomly lands on one of the predefined sections of the wheel.
- The simulation tracks the frequency of each section being landed on and calculates the probability of landing on each section.
- The probability of each section is estimated based on the number of spins that landed on it.
- The simulation also displays the distribution of outcomes, allowing for a clear understanding of the probability distribution across sections.
#### **Visualization:**
- 🍰 Pie Chart: Displays the probability of landing on each section of the wheel.
- 📊 Bar Chart: Shows the distribution of wheel spin outcomes, i.e., how many times each section was chosen.
- 🔥 Heatmap: Illustrates the frequency of landing on each section, using color gradients to indicate higher and lower frequencies.

#### **Detailed Results:**
The program prints the frequency and probability of landing on each section, offering insights into the results of the Monte Carlo simulation.

It calculates and displays the probability of landing on each section.
The most and least common sections are identified and displayed.
This simulation demonstrates how Monte Carlo methods can be applied to estimate probabilities and analyze outcomes in real-world scenarios such as games or random processes. 🎯





### 🎯 13.[Monte Carlo Simulation: Probability of Being Selected in a Competition and Answering Correctly](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_competition.py)
#### **Goal:**
Estimate the probability of a contestant being randomly selected in a competition and their likelihood of answering a multiple-choice question correctly.

#### **How It Works:**
- Simulates a large number of competitions (default: 100,000 simulations).
- Each simulation randomly selects a contestant from a fixed number of participants.
- The probability of each contestant being chosen is calculated based on frequency.
- The probability of the selected contestant correctly answering the question is computed using the assumption that they randomly guess among multiple-choice options.
- The simulation provides insights into the likelihood of contestants being chosen and answering correctly.
#### **Visualization:**
- 📊 Bar Chart (Selection Probability): Displays the probability distribution of contestants being selected.
- 📊 Bar Chart (Correct Answer Probability): Shows the probability of a contestant being chosen and knowing the correct answer.
- 🔥 Heatmap: Illustrates the frequency of contestant selection, with color gradients indicating higher and lower occurrences.

#### **Detailed Results:**
- The frequency and probability of each contestant being selected are displayed.
- The probability of answering correctly is computed based on contestant selection probability and the number of answer choices.
- The simulation identifies the most and least frequently selected contestants.
- Monte Carlo methods are used to approximate real-world probabilities in random selection and multiple-choice answering scenarios. 🎯

🚀 This simulation showcases how randomness influences outcomes in competitions and games, helping to estimate real-world probabilities through repeated trials.

### 📐 14.[Monte Carlo Simulation: Estimating the Area of a Right Triangle](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_area_of_right_triangle.py)

**Goal:** Approximate the area of a right triangle inside a unit square using a Monte Carlo method.

### 🎯 How It Works:
- A unit square (1x1) is defined.
- A right triangle is formed with vertices at (0,0), (1,0), and (1,1).
- Random points are generated within the unit square.
- The fraction of points that fall within the right triangle is used to estimate its area.

The theoretical area of the right triangle is:

 
 The area of a right triangle is calculated using the formula:

  𝐴 =1/2 × Base × Height
where the base and height are the two perpendicular sides of the triangle.

In a unit square, the ratio of points that fall below the line 𝑥=𝑦 to the total number of points represents the area of the right triangle formed within the square. In the simulation, we estimate this area by calculating the proportion of randomly generated points that satisfy 𝑥≥𝑦

- The Monte Carlo estimation should converge to 0.5 as the number of points increases.

### 📊 Visualization:
- 🟪 **Purple - Blue Square**: Represents the unit square.
- 🟦 **Light Blue Triangle**: Represents the right triangle.
-  **Scatter Points**:
  - 🟣Points **inside** the triangle are marked with one color.
  - 🟢Points **outside** the triangle are marked with another.

### 📌 Results:
- Displays the estimated area of the right triangle based on the simulation.
- Compares the Monte Carlo result with the true theoretical area.
- Shows a visual representation of the simulation.

This experiment highlights how Monte Carlo methods can be applied to geometric problems and probability-based estimations. 🎲📏

### 🔢 15.[Monte Carlo Simulation: Estimating the Value of π (Pi)](https://github.com/BetulKarakaya/MonteCarloSimulation/blob/main/simulation_of_pi.py)

**Goal:** Estimate the mathematical constant π using a Monte Carlo simulation.

### 🎯 How It Works:
- Randomly generates a large number of points within a square of side length 2.
- Determines whether each point falls inside the unit circle (radius = 1, centered at the origin).
- The ratio of points inside the circle to the total number of points is used to approximate π using the formula:

 pi ≈ 4 × [(points inside of right- top quarter) / points outside of right-top quarter]
- The estimated value of π converges towards 3.14159 as the number of points increases.

### 📊 Visualization:
- 🟢 **Green Points**: Points inside the unit circle.
- 🔵 **Blue Points**: Points outside the unit circle.
- ⚫ **Black Circle**: Represents the actual boundary of the unit circle.

The more points we simulate, the closer the estimated value of π is to its true value.

### 📌 Results:
- The program calculates an estimated value of π and compares it with the true mathematical value.
- Displays the ratio of points inside the circle vs. total points.
- Plots a scatter plot to visualize the distribution of points inside and outside the circle.

This simulation demonstrates the power of Monte Carlo methods in solving mathematical problems through random sampling. 🎲✨




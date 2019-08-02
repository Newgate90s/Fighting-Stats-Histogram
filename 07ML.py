import numpy as np
import matplotlib.pyplot as plt

# Print statements to inform the user how the histogram is made and meant to be read
print("-" * 120)
print("Average strikes landed per fighter type histogram.")
print("-" * 120)
print("Info: This is a histogram made to showcase the average amount of strikes landed for three different fighting styles. ")
print("-" * 120)
print("Data used: Every MMA fight has an average amount of strikes landed. these averages is what were used.")
print("-" * 120)
print("Data description: Every fighting style has their strengths and weaknesses.")
print("Because of this, they stick to what they're strong in.")
print("Meaning, a kicker wouldn't strike often, and a striker wouldn't kick often")
print("-" * 120)
print("Dataset values: ")
print("\nStriker average landed strikes = 150 + or - 30")
print("Grappler average landed strikes = 50 + or - 35")
print("Kicker average landed strikes = 75 + or - 40")
print("-" * 120)
print("Histogram legend:")
print("\nBlue = Striker")
print("Red = Grappler")
print("Green = Kicker")

# Three types of datasets
# The datasets are for different types of martial arts fighters
# Creating a data set of 1000 values for each type
striker = 1000
grappler = 1000
kicker = 1000


# Using the average landed strikes per fight to classify each type
striker__landed_strikes = 150 + 30 * np.random.randn(striker)
grappler_landed_strikes = 50 + 35 * np.random.randn(grappler)
kicker_landed_strikes = 75 + 40 * np.random.rand(kicker)

# Histogram for our three types of fighters
# Each type is given a color
# Striker = blue, grappler = red, kicker = green
plt.hist([striker__landed_strikes, grappler_landed_strikes, kicker_landed_strikes], stacked=True, color=['b', 'r', 'g'])
plt.show()

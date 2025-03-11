from die import Die
import plotly.express as px

# Create a D6.
die = Die()

# Number of rolls
num_rolls = 1000

# Make some rolls, and store results in a list.
results = []
for roll_num in range(num_rolls):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Print the results.
print(f"Results: {results}")
print(f"Frequencies: {frequencies}")

# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
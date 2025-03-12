import matplotlib.pyplot as plt
data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]

# Create a histogram
plt.hist(data, bins=5)

# Labeling the axes and the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Show the plot
plt.show()
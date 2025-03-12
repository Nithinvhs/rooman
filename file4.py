import matplotlib.pyplot as plt
# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [4, 7, 3, 6]

# Create a bar plot
plt.bar(categories, values)

# Labeling the axes and the plot
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')

# Show the plot
plt.show()
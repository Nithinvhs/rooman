import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
categories = ['A', 'B', 'C', 'D']
values = [5, 3, 9, 6]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [10, 15, 7, 5]

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# First subplot: Line plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

# Second subplot: Bar plot
axs[0, 1].bar(categories, values)
axs[0, 1].set_title('Bar Plot')

# Third subplot: Scatter plot
axs[1, 0].scatter(x, y)
axs[1, 0].set_title('Scatter Plot')

# Fourth subplot: Pie chart
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%')
axs[1, 1].set_title('Pie Chart')

# Show the plots
plt.show()
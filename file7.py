import matplotlib.pyplot as plt
# Data
labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [10, 15, 7, 5]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Title
plt.title('Fruit Pie Chart')

# Show the plot
plt.show()
import matplotlib.pyplot as plt

# Create a list of fruits and their corresponding quantities
fruits = ["Mango", "Apple", "Grapes", "Banana"]
quantities = [30, 25, 30, 15]

# Create a pie chart
plt.pie(quantities, labels=fruits)

# Add a title to the pie chart
plt.title("Fruits")

# Add labels to the pie chart segments
for i in range(len(fruits)):
  plt.annotate(fruits[i], (quantities[i]/2, (sum(quantities) - quantities[i])/2))

# Add a legend to the pie chart
plt.legend()

# Show the pie chart
plt.show()

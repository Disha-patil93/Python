import numpy as np

# Create a 3x3 NumPy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the column wise mean
mean = np.mean(array, axis=0)

# Calculate the column wise median
median = np.median(array, axis=0)

# Print the column wise mean and median
print("Column wise mean:")
print(mean)

print("Column wise median:")
print(median)

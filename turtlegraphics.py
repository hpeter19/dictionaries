import matplotlib.pyplot as plt
import numpy as np

# Generate random data
val = np.random.randint(1, 10, 5)

# Customize the plot
plt.figure(figsize=(8, 5))
bars = plt.bar(range(len(val)), val, color=['red', 'green', 'blue', 'purple', 'orange'])

# Add bar labels
for i, v in enumerate(val):
    plt.text(i, v + 0.1, str(v), ha='center')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Customized Random Bar Plot')

# Show the plot
plt.show()
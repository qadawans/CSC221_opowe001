# 15-2

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.flag, s=10)

# Set chart title and label axes. 
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis. 
ax.axis([0, 1100, 0, 1_100_000])

plt.show()
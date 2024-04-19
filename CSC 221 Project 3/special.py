# special.py

import numpy as np
import matplotlib.pyplot as plt

# How old my friends and family are
x_data = ['Lizzy', 'Jane', 'Jayden', 'Emily', 'Amanda', 'Emma', 'Tobey', 'Tyler']
y_data = [18, 18, 18, 26, 32, 20, 21, 21]

# Define a colormap
colormap = 'cool'  

# Plot the data as a bar graph with colormap
plt.bar(x_data, y_data, color=plt.cm.get_cmap(colormap)(y_data))

# Add labels and title
plt.xlabel('Names')  
plt.ylabel('Ages') 
plt.title('How Old My Friends and Family Are') 

# Show the plot
plt.show()

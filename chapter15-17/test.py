import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Use a built-in matplotlib style

# Make data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
mental_health_scores = [5, 4, 3, 2, 1, 1, 1]

# Manually create a color map
colors = ['#440154', '#3b528b', '#21918c', '#5ec962', '#fde725', '#ffbc42', '#f95d6a']

# Plot
fig, ax = plt.subplots(figsize=(12, 6))

# Set darker background color
ax.set_facecolor('#d3d3d3')  # Darker shade of gray

# Plot with colors
for i in range(len(days)):
    ax.plot(days[i], mental_health_scores[i], 'o', color=colors[i], markersize=10)
ax.plot(days, mental_health_scores, '-', color='red', linewidth=2.5, label='Mental Health Declining')

# Set y-axis limits and ticks
ax.set(ylim=(0, 6), yticks=range(0, 7))

# Add titles and labels
ax.set_title('Mental Health Trends Over the Week', fontsize=20, color='darkblue', weight='bold')
ax.set_xlabel('Days of the Week', fontsize=16, weight='bold')
ax.set_ylabel('Mental Health Score', fontsize=16, weight='bold')

# Add grid
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper right', fontsize=12)

# Show the plot
plt.show()
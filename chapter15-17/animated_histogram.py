import plotly.express as px
import pandas as pd
import numpy as np

# Generate random data
data = pd.DataFrame({
    "Value": np.random.randn(1000),
    "Frame": np.repeat(range(1, 21), 50)  # Simulate frame numbers
})

# Create an animated histogram
fig = px.histogram(
    data,
    x="Value",
    animation_frame="Frame",  # Animate over frames
    nbins=30,
    range_x=[-4, 4],
    color_discrete_sequence=["skyblue"]
)

# Customize appearance
fig.update_layout(
    title="Animated Histogram",
    xaxis_title="Value",
    yaxis_title="Frequency",
    plot_bgcolor='whitesmoke'
)

# Show the histogram
fig.show()

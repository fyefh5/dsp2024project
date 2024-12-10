
import numpy as np
import plotly.graph_objects as go

# Parameters
N = 80  # Number of iterations
angles = np.linspace(0, 2 * np.pi * (N - 1) / N, N)  # Angles for the rotations
radius = 1

# Trigonometric circle points
circle_x = np.cos(np.linspace(0, 2 * np.pi, 100))
circle_y = np.sin(np.linspace(0, 2 * np.pi, 100))

# Create frames for animation
frames = []
for i in range(N):
    x_vector = [0, radius * np.cos(angles[i])]
    y_vector = [0, radius * np.sin(angles[i])]
    frame = go.Frame(
        data=[
            go.Scatter(x=circle_x, y=circle_y, mode="lines", name="Circle"),
            go.Scatter(x=x_vector, y=y_vector, mode="lines+markers", name="Vector"),
            go.Scatter(x=[radius * np.cos(angles[i])], y=[radius * np.sin(angles[i])], mode="markers"),
        ],
        layout=go.Layout(
            annotations=[
                dict(
                    x=0.5,
                    y=1.2,
                    xref="paper",
                    yref="paper",
                    text=f"Iteration: {i}",
                    showarrow=False,
                    font=dict(size=14),
                )
            ]
        ),
    )
    frames.append(frame)

# Create figure
fig = go.Figure(
    data=[
        go.Scatter(x=circle_x, y=circle_y, mode="lines", name="Circle"),
        go.Scatter(x=[0, radius], y=[0, 0], mode="lines+markers", name="Vector"),
    ],
    layout=go.Layout(
        title="Trigonometric Circle with Animation",
        xaxis=dict(range=[-1.2, 1.2], zeroline=False),
        yaxis=dict(range=[-1.2, 1.2], zeroline=False, scaleanchor="x"),
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate", args=[None]),
                    dict(label="Pause", method="animate", args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")]),
                ],
            )
        ],
    ),
    frames=frames,
)

# Show figure
fig.show()

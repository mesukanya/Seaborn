import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import numpy as np

plotly.tools.set_credentials_file(username='sukanya_123', api_key='ElCUcA4FbCNvUWCdXDMD')


N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-scatter')



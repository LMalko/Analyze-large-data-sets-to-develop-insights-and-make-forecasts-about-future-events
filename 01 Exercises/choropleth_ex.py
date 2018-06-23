import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly as py
import plotly.graph_objs as go
import cufflinks as cf

from plotly.offline import download_plotlyjs, \
    init_notebook_mode,\
    plot,\
    iplot

init_notebook_mode(connected=True)

cf.go_offline()


data = dict(type="choropleth",
            locations = ["AZ", "CA", "NY", "MT"],
            locationmode = "USA-states",
            colorscale = "Jet",
            text = ["text 1", "text 2", "text3"],
            z = [1.0, 2.0, 3.0],
            colorbar = {"title": "Colorbar goes here"})

layout = dict(geo={"scope": "usa"})

choromap = go.Figure(data = [data], layout=layout)


py.offline.plot(choromap)

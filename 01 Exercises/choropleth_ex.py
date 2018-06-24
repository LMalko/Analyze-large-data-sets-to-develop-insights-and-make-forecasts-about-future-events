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
            locations = ["AZ", "CA", "NY", "FL"],
            locationmode = "USA-states",
            colorscale = "Greens",
            text = ["text 1", "text 2", "text3", "text4"],
            z = [1.0, 1.5, 2.0, 1.5],
            colorbar = {"title": "Colorbar goes here"})

layout = dict(geo={"scope": "usa"})

# choromap = go.Figure(data = [data], layout=layout)
#
#
# py.offline.plot(choromap)


df = pd.read_csv("2011_US_AGRI_Exports.csv")

data2 = dict(type="choropleth",
            colorscale="YIOrRd",
            locations = df["code"],
            locationmode = "USA-states",
            z = df["total exports"],
            text = df["text"],
            colorbar = {"title": "Millions USD"},
            marker = dict(line =
                          dict(color = "black",
                               width=5)))

layout2 = dict(title = "2011 USA Agriculture Exports by State",
              geo = dict(scope="usa",
                         showlakes = True, lakecolor="rgb(85, 173, 240)"))

# choromap2 = go.Figure(data = [data2], layout=layout2)
#
#
# py.offline.plot(choromap2)


df = pd.read_csv("2014_World_GDP.csv")

data3 = dict(type="choropleth",
            colorscale="YIOrRd",
            locations = df["CODE"],
            z = df["GDP (BILLIONS)"],
            text = df["COUNTRY"],
            colorbar = {"title": "GDP in Billions USD"})


layout3 = dict(title = "2014 Global GDP",
              geo = dict(showframe=False,
                         projection={"type": "Mercator"}))

choromap3 = go.Figure(data = [data3], layout=layout3)


py.offline.plot(choromap3)
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
#
# choromap3 = go.Figure(data = [data3], layout=layout3)
#
#
# py.offline.plot(choromap3)


df = pd.read_csv("2014_World_Power_Consumption.csv")


# df.head()


data4 = dict(type="choropleth",
            colorscale="Viridis",
            locations = df["Country"],
            reversescale = True,
            locationmode = "country names",
            z = df["Power Consumption KWH"],
            text = df["Text"],
            colorbar = {"title": "Power Consumption"})

layout4 = dict(title = "Power Consumption",
              geo = dict(showframe=False,
                         projection={"type": "Mercator"}))

# choromap4 = go.Figure(data = [data4], layout=layout4)
#
#
# py.offline.plot(choromap4)



df5 = pd.read_csv("2012_Election_Data.csv")

# df.head()


data5 = dict(type="choropleth",
            colorscale="Viridis",
            reversescale = True,
            locations = df5["State Abv"],
            locationmode = "USA-states",
            z = df5['Voting-Age Population (VAP)'],
            text = df5["State"],
            colorbar = {"title": "Voting-Age Population (VAP)"},
            marker = dict(line =
                          dict(color = 'rgb(255,255,255)',
                               width = 1)),)

layout5 = dict(title = "Voting-Age Population",
              geo = dict(scope="usa",
                         showlakes = True,
                         lakecolor="rgb(85, 173, 240)"))


choromap5 = go.Figure(data = [data5], layout=layout5)


py.offline.plot(choromap5)
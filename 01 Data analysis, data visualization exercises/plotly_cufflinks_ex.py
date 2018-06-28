# Cufflinks connects plotly with pandas.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly as py

import cufflinks as cf

from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)

cf.go_offline()

df1 = pd.DataFrame(np.random.randn(100, 4),
                  columns="A B C D".split())

df2 = pd.DataFrame({"Category": ["A", "B","C"],
                    "Values": [32, 43, 56]})




# fig = df1.iplot(bins=50, asFigure=True)
# py.offline.plot(fig)

# fig = df1.iplot(kind="scatter", x="A", y="B",
#                 mode="markers", size=20, bins=50, asFigure=True)
# py.offline.plot(fig)

# fig = df2.iplot(kind="bar", x="Category", y="Values",
#                 bins=50, asFigure=True)
# py.offline.plot(fig)

# fig = df1.sum().iplot(kind="bar", asFigure=True)
# py.offline.plot(fig)

# fig = df2.count().iplot(kind="bar", asFigure=True)
# py.offline.plot(fig)

# fig = df1.iplot(kind="box", asFigure=True)
# py.offline.plot(fig)

# 3 dimensions
df3 = pd.DataFrame({"x": [1,2,3,4,5], "y": [10,20,30,40,50],
                    "z": [500, 400, 300, 200, 100]})

# fig = df3.iplot(kind="surface", asFigure=True,
#                 colorscale="rdylgn")
# py.offline.plot(fig)

# fig = df1.iplot(kind="hist", asFigure=True, bins=50)
# py.offline.plot(fig)

# fig = df1["A"].iplot(kind="hist", asFigure=True, bins=50)
# py.offline.plot(fig)

# fig = df1[["A", "B"]].iplot(kind="spread",
#                             asFigure=True)
# py.offline.plot(fig)

# fig = df1.iplot(kind="bubble", asFigure=True,
#                 x="A", y="B", size="C")
# py.offline.plot(fig)




import plotly.figure_factory as ff

# fig = ff.create_scatterplotmatrix(df1, height=1000,
#                                   width=1000, diag="histogram",
#                                   size=3, fillcolor="red")


# scatter_matrix() on jupiter:
# Similar to sns.pairplot()
# df.scatter_matrix()


import plotly.graph_objs as go
#
# trace1 = go.Scatter3d(
#     x=df3["x"],y=df3["y"],z=df3["z"],
#     mode='markers',
#     marker=dict(
#         size=12,
#         line=dict(
#             color='rgba(217, 217, 217, 0.14)',
#             width=0.5
#         ),opacity=0.8))
# data = [trace1]
# fig = go.Figure(data=data)









pl_colorscale=[[0.0, '#19d3f3'],
               [0.333, '#19d3f3'],
               [0.333, '#e763fa'],
               [0.666, '#e763fa'],
               [0.666, '#636efa'],
               [1, '#636efa']]


trace1 = go.Splom(dimensions=[dict(label='sepal length',
                                 values=df1["A"]),
                            dict(label='sepal width',
                                 values=df1["B"]),
                            dict(label='petal ngth',
                                 values=df1["C"]),
                            dict(label='petal len',
                                 values=df1["D"])],
                marker=dict(
                            color="green",
                            size=7,
                            colorscale=pl_colorscale,
                            showscale=False,
                            line=dict(width=0.5,
                                      color='red'))
                )

axis = dict(showline=True,
          zeroline=False,
          gridcolor='yellow',
          ticklen=4)

layout = go.Layout(
    title='Iris Data set',
    dragmode='select',
    width=600,
    height=600,
    autosize=False,
    hovermode='closest',
    plot_bgcolor='lightgrey',
    xaxis1=dict(axis),
    xaxis2=dict(axis),
    xaxis3=dict(axis),
    xaxis4=dict(axis),
    yaxis1=dict(axis),
    yaxis2=dict(axis),
    yaxis3=dict(axis),
    yaxis4=dict(axis)
)

fig = dict(data=[trace1], layout=layout)


py.offline.plot(fig)

plt.show()






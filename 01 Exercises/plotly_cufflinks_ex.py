# Cufflinks connects plotly with pandas.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly as py
from plotly import __version__

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

df3 = 
plt.show()






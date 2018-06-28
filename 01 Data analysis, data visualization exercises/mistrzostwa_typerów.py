import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd



fig, axes = plt.subplots(figsize=(5,5))

dzien_mistrzostw = [0, 1, 2, 3, 4, 5, 6, 7]

Jarek_pkt = [0, 1, 1, 2, 0, 5, 1, 3]
PJ_pkt = [0, 0, 2, 4, 1, 3, 3, 3]
Jacek_pkt = [0, 1, 1, 2, 1, 3, 1, 3]
Niger_pkt = [0, 1, 1, 6, 3, 4, 1, 3]

# from itertools import accumulate
#
# new_l = accumulate(lista)


Jarek = np.cumsum(Jarek_pkt)
PJ = np.cumsum(PJ_pkt)
Jacek = np.cumsum(Jacek_pkt)
Niger = np.cumsum(Niger_pkt)

axes.plot(dzien_mistrzostw, Jarek, label="Jarek")
axes.plot(dzien_mistrzostw, PJ, label="PJ")
axes.plot(dzien_mistrzostw, Jacek, label="Jacek")
axes.plot(dzien_mistrzostw, Niger, label="Niger")

axes.set_ylabel("Punkty razem")
axes.set_xlabel("Dni mistrzostw")
axes.set_title("Mistrzostwa swiata typerów")

axes.legend()

axes.yaxis.set_major_formatter(FormatStrFormatter('%d'))
axes.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

plt.xticks(np.arange(min(dzien_mistrzostw), max(dzien_mistrzostw)+1, 1.0))

# 2nd graph

fig2, axes = plt.subplots(figsize=(5,5))

axes.plot(dzien_mistrzostw, Jarek_pkt, label="Jarek")
axes.plot(dzien_mistrzostw, PJ_pkt, label="PJ")
axes.plot(dzien_mistrzostw, Jacek_pkt, label="Jacek")
axes.plot(dzien_mistrzostw, Niger_pkt, label="Niger")

axes.set_ylabel("Punkty w dniu")
axes.set_xlabel("Dni mistrzostw")
axes.set_title("Mistrzostwa swiata typerów")

axes.yaxis.set_major_formatter(FormatStrFormatter('%d'))
axes.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

plt.xticks(np.arange(
    min(dzien_mistrzostw),
    max(dzien_mistrzostw)+1, 1.0))


axes.legend()

plt.show()




# plt.close()
# tips = pd.read_excel('ms.xlsx')
# sns.distplot(tips['Niger'])
# plt.show()
# sns.distplot(tips['Piotrek'])
# plt.show()
# sns.distplot(tips['Jacek'])
# plt.show()
# sns.distplot(tips['Jarek'])
# plt.show()
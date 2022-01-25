import matplotlib.pylab as plt
from matplotlib.pyplot import axes, figure
y=[
    14036.85,14003.22,14055.95,
    14045.58,15015.65,16693.24
]
x=[
    2015,2016,2017,
    2018,2019,2020
]
figure,axes=plt.subplots()
axes.plot(x,y)
axes.set_ylabel("Penggangguran")
axes.set_xlabel("Tahun")
axes.set_title("Penggangguran Di Indonesia 2015-2020")
plt.show()
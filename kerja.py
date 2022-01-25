from matplotlib.pyplot import axes, axis, figure
import pandas as pd
import matplotlib.pylab as plt
import numpy as py

Tingkat_pendidikan=["<=SD","SMP","SMA","SMK","DIPLOMA","UNIVERSITAS"]
Data=[66.21,53.27,37.64,30.24,18.58,11.19]

figure,axes=plt.subplots()
axes.pie(
    Data,labels= Tingkat_pendidikan,
    autopct="%.2f%%"
    )
plt.show()
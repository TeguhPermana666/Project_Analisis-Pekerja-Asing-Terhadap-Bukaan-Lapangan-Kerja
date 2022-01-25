import pandas as pd
import matplotlib.pylab as plt
from matplotlib.pyplot import axes, axis, figure
negara=["MALAYSIA","TAIWAN","HONGKONG","UAE","OMAN","QATAR",
"UNITED STATES","BAHRAIN","ITALY","KUWAIT","TURKEY","JAPAN","SPAIN","CHINA",
"SOUTH AFRICA","THAILAND"]

tenaga=[98.58,74.05,41.58,151.16,155.40,119.94,124.25,68.41,171.20,240.21,
262.47,308.29,298.60,238.80,228.00,166.00]
figure,axes=plt.subplots()
#membuat diagram dengan lingkaran
axes.pie(
    tenaga,labels=negara,
    autopct="%.2f%%"
    )
#melihatkan data
plt.show()
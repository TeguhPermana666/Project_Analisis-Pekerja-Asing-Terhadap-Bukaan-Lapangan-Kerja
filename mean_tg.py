import pandas as pd
import numpy as np

Data_Indonesia=pd.ExcelFile("D:/Data Analysis/TeguhPermana_data/Project/data_migran.xlsx")
Data_Indonesia=Data_Indonesia.parse("Table 2")

Data_Indonesia=Data_Indonesia[Data_Indonesia["NEGARA"]=="THAILAND"]
print(Data_Indonesia)

total_kasus=Data_Indonesia.iloc[:,2:7].values[0]
print(total_kasus)
mean=sum(total_kasus)/len(total_kasus)
print("Rata rata total kasus adalah {:.2f} ribu".format(mean))
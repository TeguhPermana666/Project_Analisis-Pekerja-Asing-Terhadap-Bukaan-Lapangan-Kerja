import pandas as pd
penggangguran={"2015":[14036.85],"2016":[14003.22],"2017":[14055.95],"2018":[14045.58],"2019":[15015.65],"2020":[16693.24]}
df=pd.DataFrame.from_dict(penggangguran,orient="index",columns=["Penggangguran"])
print(df)
df.to_excel("D:/Data Analysis/TeguhPermana_data/Project/Data_Penggangguran.xlsx",index=False)




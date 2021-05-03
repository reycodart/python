#            DataFrameler ile Çalışma

import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

#-------------------------

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df["Column1"]
result = df.iloc[2] # iloc => indeks gösterir.
result = df.loc["A","Column2"] # İkisinin kesiştiği yeri gösterir.
result = df.loc[["A","B"],["Column1","Column2"]]# A,B satırlarının Column1,2 leri getir demek.


# loc kullanımı şöyle:
# loc["row","column"] => ikisi bir böyle yapılır.
# loc["row"]  => sadece row da seçilebilir.
# loc[:,"column"] => sadece column kullanımı da böyle olur.

result  = df.loc["A"] # loc: location demek, [] ile kullanılır.
result = df.loc[:,"Column1"] # result = df["Column1"] (yapılanların ikiside yanı şey)
result = df.loc[:,["Column1","Column2"]]

# Belirli bir aralıktaki column almak istersek şöyle :
result = df.loc[:,"Column1":"Column3"]

# Belirli bir aralıktaki satır almak istersek şöyle : 
result = df.loc["A":"B",:"Column2"]

#Column eklemek istersek şöyle:
df["Column4"] = pd.Series(randn(3), ["A","B","C"])

# Column silmek istersek şöyle:
df.drop("Column4", axis=1, inplace=True) # Kolonun yukardan aşağı diye 1 verdik.
# inplace = False dersek o kolonu kopyasını çıkartır.

print(result)
print(df)














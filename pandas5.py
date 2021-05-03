#                 DataFrame Filtreleme

import pandas as pd
import numpy as np  

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])
result = df

result = df.columns # Dosya içindeki kolonları gösterir.
result = df.head() # İlk 5 satırı getirir.
result = df.head(10) # ilk 10 satırı getirir.
result = df.tail()# son 5 satırı getirir.
result = df["Column1"].head()

# Birden fazla kolon almak için:
result = df[["Column1","Column2"]].head()

#DataFrame parçalama işlemi:
result = df[5:15][["Column1","Column2"]].tail()

#----------------------------------------------


# DataFrame 'in içindeki datalar üzerinden filtreleme nasıl yapılır?

result = df > 50 # 50 değerinden büyükleriçin True yazdırır.Diğerleri için False
result = df[df > 50] # False olanları göstermez.(NaN yazar.)
result = df[df %2 == 0]
result = df["Column1"] > 50 # True-False döndürür.
result = df[df["Column1"] > 50]# sadece 50 den büyükleri gösterir.
result = df[df["Column1"] > 50][["Column1","Column2"]]# Kolonlarıda filtreler.
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)]# | işareti = or(ya da)
result = df.query("Column1 >= 50 & Column1 % 2 == 0")["Column1"]

print(result)






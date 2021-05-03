#             DATA FRAME

# İki tane seriyi toplayınca bir dataframe elde ediyoruz.

import pandas as pd


list = [["Ahmet",26], ["Ayşe",54], ["Fatma",78]]

#df = pd.DataFrame()
#df = pd.DataFrame([1,2,3,4]) Kolon ismi olm için 0 dan başlar.
df = pd.DataFrame(list, columns = ['Name','Grade'], index = [1,2,3], dtype = float)

# Aynı şeyi dict ile de yapabilriz:

dict = {"Name": ["Ahmet","Ayşe","Fatma"], "GRade": [26,54,78]}
df = pd.DataFrame(dict)


print(df)


#----------------
"""

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)

"""





























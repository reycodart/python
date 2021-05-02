#                         SERİES   

import pandas as pd

# data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
# letter = ['a',25] heterojen old için sorun olmaz.
scalar = 5
dict = {'t':1,'r':2,'k':3,'y':4}


# pandas_series = pd.Series()
#pandas_series = pd.Series(numbers)
#pandas_series = pd.Series(letters)
#pandas_series = pd.Series(scalar)# ya da (5) yazmakta yeterlidir.
pandas_series = pd.Series(dict)#indeksleri zaten var.


#pandas_series = pd.Series(5, [0,1,2,3,4])# Atadığımız indekslerin hepsine 5 yazar.


pandas_series = pd.Series(numbers, ['ç','ş','ö','q'])
#Not: numbersta olan değer kaç taneyse o kadar indeks atanmalıdır.


pandas_series = pd.Series([20,30,40,50], ['a','b','c','d'])
result = pandas_series[0]#indeks no farklı ama yine de 0 deyince 20yi verir.
result = pandas_series[-2:]# son iki elamını alır.
result = pandas_series['d']# d ye karşılık gelen 50 yazdırılır.
result = pandas_series.ndim # boyutunu söyler.
result = pandas_series.sum()# toplamını söyler yani bu ör için 140
result = pandas_series + 100# hepsine 100 atanır.

print(pandas_series)
print(result)

#--------

# örnek:

opel2018 = pd.Series([20,30,40,10],['astra','corsa','mokka','insignia'])
opel2019 = pd.Series([40,30,20,10],['astra','corsa','Grandland','insignia'])

total = opel2018 + opel2019

print(total)
print(['astra'])







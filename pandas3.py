#                 Farklı Dosya Tiplerinden Veri Okuma

import pandas as pd
import sqlite3


#          csv dosyasında:

df = pd.read_csv('Dosya_adı')

print(df)

#--------------------

#          json dosyasında:

df = pd.read_json('Dosya_adı',encoding="UTF-8")

print(df)

#--------------------

#          excel dosyasında:

df = pd.read_excel('Dosya_adı')

print(df)

# Not: ecel dosyalarını okuyabilmek için terminale pip install xlrd yaz ve indir.

#----------------

#               sqlite dosyasında:

connection = sqlite3.connect('Dosya_adı')

df = pd.read_sql_query("SELECT * FROM students",connection)
# students tablosundan bir bilgi okumak için.

print(df)










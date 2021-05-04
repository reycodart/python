import numpy as np

#                       Diziler

# result = np.array([1,3,5,7,9]) => Bunu kendimiz oluşturduk.

result = np.arange(1,10) # arange 1-10 arası bir dizi yapar.

result = np.arange(10,100,5)# 10-100 arasında artış miktarı 5 olan dizi.

result = np.zeros(10)# 10 tane sıfırdan olşan dizi.

result = np.ones(5)# 5 tane birden oluşan dizi.

result = np.linspace(0,100,5)#0-100 arasını 5 eşit parçaya böl.
result = np.linspace(0,5,5)

result = np.random.randint(0,10) #0-10 arası rastgele sayı üretir.
result = np.random.randint(20)# bu da aynısını yapar tek parametre olmasına rağmen.
result = np.random.randint(1,10,3)#1-10 arası rastgele 3 sayı getirir.

result = np.random.rand(5)#rand 0-1 arası sayı üretir ör: 5 tane dedik.
result = np.random.randn(5)#randn (-) değerleri de katar.

print(result)

np_array = np.arange(50)
np_multi = np_array.reshape(5,10)
print(np_multi.sum(axis = 1)) # axis = 1 demek sütun
print(np_multi.sum(axis = 0)) # axis = 1 demek satır
 
#----------------------------------

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.min()
result = rnd_numbers.max()
result = rnd_numbers.mean()# ortalamayı verir.
result = rnd_numbers.argmax()# en büyük sayının indeks no.sunu söyler.
result = rnd_numbers.argmin()# en küçük sayının indeks no.sunu söyler.
print(result)
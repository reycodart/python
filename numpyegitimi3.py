#      Dizilerin İndekslenmesi

import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5] #5. indeksi verir.
result = numbers[-1] # en son indeksi verir.yani 75
result = numbers[:3] # baştan ilk 3 indeksi verir.
result = numbers[0:3] # baştan ilk 3 indeksi verir.
result = numbers[3:] # sondaki ilk 3 indeksi verir.
result = numbers[::] # bütün liste yazdırılır.
result = numbers[::-1] # listeyi ters çevirir.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,100]])

result = numbers2[0]
result = numbers2[2]# 2. satırı ifade eder.
result = numbers2[0,2]# 0. satırın 1. indeksi
result = numbers2[:,2]# Tüm satırları seçer 2. indkstekini alır.
result = numbers2[:,0:2]# Tüm satırları seç, 0 ve 2. indesktekileri al.
result = numbers2[-1,:]# Son satırın tüm sütunlarını alır.
result = numbers2[:2,:2]# cvp : [0,5] [15,20]

print(result)

#-----------------------------------------------

arr1 = np.arange(0,10)
arr2 = arr1 # referans

arr2 = arr1.copy()# Böyle yapılınca değişiklik sadece arr2 de olur.
arr2[0] = 20 # arr1 e de aynı şey olur.

# NOT: İkisi de aynı içeriği gösteriyor. Çünkü aynı adresteler.
# yani cvp: [1,2,3,4,5,6,7,8,9] olur.

print(arr1)
print(arr2)

#             Dizi Operasyonları

import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1, numbers2)

result = numbers1 + numbers2
result = numbers1 + 50 # numbers1 dekilerin hepsine 50 eklenir.
result = numbers1 - numbers2 # Farkını alır.

result = np.sin(numbers1)# sinüsünü alır.
result = np.sqrt(numbers1)# Karekökünü alır.

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1, multi_numbers2)

result = np.vstack((multi_numbers1,multi_numbers2))# Dikey olarak birleştirir.
result = np.hstack((multi_numbers1,multi_numbers2))# Yatay olarak birleştirir.

result = numbers1 >= 5 # bool türünde değer döndürür.
result = numbers1 % 2 == 0 # çitf olup olmadığını sorar, bool türünde cvp verir.
print(numbers1[result])# Direkt True değerleri gösterir.
print(result)# Aynı indeksteki sayıları toplar ve yazar.

import numpy as np 

#                 Numpy Kullanımı

#pythonn list
py_list = [1,2,3,4,5,6,7,8,9] # tek boyutlu

# numpy array da artık liste yerine dizi kullanılacak.
np_array = np.array([1,2,3,4,5,6,7,8,9])# Parametre olrk içine liste şeklinde yollanır.
#        bu dizi de tek boyutludur.

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)#3 e 3 lük matrkis oluşur.

print(py_multi)
print(np_multi)

print(np_array.ndim)# Kaç boyutu var? bir boyutlu
print(np_multi.ndim)# 2 boyutlu

print(np_array.shape)# boyutu (9,)
print(np_multi.shape)#(3,3)

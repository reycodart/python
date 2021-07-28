

import urllib.request
import os

# eğer fotograflar adında bir klasör yoksa oluşturmak için
if not os.path.exists("logo"):
    os.makedirs("logo")

url = input("URL: ")

a = urllib.request.urlretrieve(url, "logo/w2.jpg")


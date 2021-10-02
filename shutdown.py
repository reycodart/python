import os
import pyttsx3

sec = 5
os.system(f'shutdown /s /t {sec}')
pyttsx3.speak(f'Bilgisayarını {sec} saniye sonra kapatıyorumm')


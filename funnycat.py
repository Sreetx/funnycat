
"""Software yang kami buat bersifat open source"""

import os, time, sys, re
os.system(' ')

print ("\n [*] Memulai Program....\n")
time.sleep(3)
print (" [..............................] 0%")
time.sleep(3)
print (" [>>>>>>>>>>>>>>>>>>............] 62%")
try:
    import requests
except ImportError: print ("\n [!] Kamu tidak memiliki module requests. Harap install module requetst terlebih dahulu\n");sys.exit()
time.sleep(4)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>....] 85%")
time.sleep(3)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] 100%\n")
time.sleep (3)
print (" [*] Membuka Program....\n")
time.sleep(3)

print ("#----------------------------------------------------------------#")
print ("<|------------------------| Funny Cat |-------------------------|>")
print (" | Author:             RX77E, Security Syber Team Indonean      |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

enter = input ("\n [#] Tekan enter untuk melanjutkan...\n")
ttg = open("READMIE.txt", "r")
print(ttg.read())

try:
    url = input("\n [?] Masukkan URL video yang akan didownload: ")
    print ("\n  [*] Mencari file video....")
    video = url.split('/')[-1]
    print('\n [*] Mengunduh video '+video+'.mp4....')
    fi = requests.get(url)
    with open(video+'.mp4' , 'wb') as vidio:
      vidio.write(fi.content)
    print ("\n  [*] Video berhasil di download...\n")
    print ("  [*] Video anda sudah disimpan dengan nama '"+video+".mp4'\n")
    tanya = input(" [*] Follow berbagai akun kami? [Y/n]")
    if tanya.lower() == 'y':
        webbrowser.open('https://github.com/Sreetx/')
        webbrowser.open('https://www.instagram.com/memelucubikin/')
        webbrowser.open('https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/')
        webbrowser.open('https://progpem.blogspot.com/2022/04/hom.html/')
        print (" [*] Terima kasih atas perhatian kalian")
    else:
        sys.exit()
except Exception as e: print ("   [!] Video tidak ditemukan\n");sys.exit()
except KeyboardInterrupt: print ("\n   [*] Mematikan program....");time.sleep(3);sys.exit()

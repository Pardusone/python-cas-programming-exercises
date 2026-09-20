import numpy as np
import time



poolMap=np.zeros((20,20),dtype=int)
coordinates=np.zeros((5,2),dtype=int)



poolMap[5][5]=1 #BASLANGIC
poolMap[12][7]=2 #1.HEDEF
poolMap[8][13]=2 #2.HEDEF
poolMap[10][15]=2 #3.HEDEF
poolMap[15][11]=2 #4.HEDEF


#HAVUZ KONUMLARINNIN KOORDİNAT LISTESI
coordinates[0]=[5,5]#BASLANGIÇ
coordinates[1]=[12,7]#1.HEDEF
coordinates[2]=[8,13]#2.HEDEF
coordinates[3]=[10,15]#3.HEDEF
coordinates[4]=[15,11]#4.HEDEF

araba_pozisyonu = coordinates[0]  # Araç başlangıç pozisyonu
skor = 0  # Puan başlangıç değeri

# Hedef noktalara ulaşma işlemi
for i in range(1, len(coordinates)):
    hedef = coordinates[i]
    while araba_pozisyonu[0] != hedef[0] or araba_pozisyonu[1] != hedef[1]:
        # Araç hareketi
        if araba_pozisyonu[0] < hedef[0]:
            araba_pozisyonu[0] += 1  # Kuzey yönü
        elif araba_pozisyonu[0] > hedef[0]:
            araba_pozisyonu[0] -= 1  # Güney yönü
        elif araba_pozisyonu[1] < hedef[1]:
            araba_pozisyonu[1] += 1  # Doğu yönü
        elif araba_pozisyonu[1] > hedef[1]:
            araba_pozisyonu[1] -= 1  # Batı yönü

        skor -= 1  # Hareket için 1 puan kaybı

    skor += 15  # Hedefe ulaşma için 15 puan kazanım

print("Araç puanı:", skor)
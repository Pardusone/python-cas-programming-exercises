#2 boyutlu diziler
matris = [[1,3,6],[2,7,8],[1,2,3]]
print(matris)
#Belirli bir satırı seçmek
print(matris[0]) #ilk satırı yazdırdık
#tek eleman almak
print(matris[0][2]) #ilk satır 3. elemanı yazdırdık
#matris formuna getirmek için for döngüsü kullanımı
m1 = [[2,0,3],
     [4,5,2],
     [7,0,2]
     ]
for i in range(3):
    print(m1[i])

m2 = [[3,4,5],
     [0,5,3],
     [1,2,5]
     ]
for i in range(3):
    print(m2[i])
#matrileri toplamak
m3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        m3[i][j] = m1[i][j] + m2[i][j]


for i in range(3):
    print(m3[i])
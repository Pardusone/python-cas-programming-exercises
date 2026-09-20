dizi = [0,1,2,3,4,5,6,7,8,9]

dizi[0] = 5 

print(dizi[0:5])
#dizi uzunluğu
print(len(dizi))
#string diziler
sdizi = ["elma","kahve","muz"]
print(sdizi[0]);
#eleman eklemek
sdizi.append("üzüm")
print(sdizi)
#diziden eleman silmek için
del sdizi[1]
print(sdizi)
#ya da 
sdizi.remove("üzüm") #üzüm çıkmış oldu
#ya da 
sdizi.pop(0) #indis numarası ile silme
print(sdizi)
#eleman eklemek
sdizi += ["armut","üzüm"]
print(sdizi)
#dizilerle kartezyen çarpımı 
sdizi *= 2 
print(sdizi)
#dizinin içindeki sayıları sıralamak
sayilar = [21,34,36,32,123,41,52]
sayilar.sort() #küçükten büyüye sıraladık
print(sayilar)
#diziyi ters çevirmek 
sayilar.reverse()
print(sayilar)
#dizi içerisindeki elemanların kaç defa tekra ettiğini saymak
a = sayilar.count(21) #21 kaç defa tekrar etmiş ona bakmak için
print(a)
#diziyi sıfırlamak için
sayilar.clear()
print(sayilar)
#diziye ekleme yapmak
sayilar.insert(0,12) #ilk elemana 12 ekledik
print(sayilar)
#diziye eleman eklemek için
sayilar.insert(1,23)
print(sayilar)
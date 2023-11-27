import random
import math

alt_sinir = int(input("Alt sınırı girin:"))
ust_sinir = int(input("Üst sınırı girin:"))

rastgele_sayi = random.randint(alt_sinir, ust_sinir)
tahmin_hakki = round(math.log(ust_sinir - alt_sinir + 1, 2))

print(f"\n\tSayıyı bulmak için {tahmin_hakki} hakkınız var!\n")

sayac = 0

while sayac < tahmin_hakki:
    sayac += 1

    tahmin = int(input("Tahmininizi girin:"))
    
    if tahmin == rastgele_sayi:
        print(f"Tebrikler sayıyı {sayac} tahminde buldunuz!")
        break
    elif rastgele_sayi > tahmin:
        print("Sayı tahmininizden daha büyük!")
    elif rastgele_sayi < tahmin:
        print("Sayı tahmininizden daha küçük!")

if sayac > tahmin_hakki:
    print(f"Malesef sayıyı bulamadınız.. Sayı: {rastgele_sayi}")
    
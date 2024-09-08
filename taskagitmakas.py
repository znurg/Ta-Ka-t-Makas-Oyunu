import random

hamleler = ["Taş", "Kağıt", "Makas"]
oyunSayisi = int(input("Oyun Kaç el Sürsün? "))
bilgisayarSkor = 0
oyuncuSkor = 0

for i in range(oyunSayisi):
    oyuncu = input("Taş/Kağıt/Makas ?").capitalize()
    bilgisayar = random.choice(hamleler)

    if oyuncu == "Taş" and bilgisayar == "Makas":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Tebrikler!")
        oyuncuSkor += 1
    elif oyuncu == "Makas" and bilgisayar == "Kağıt":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Tebrikler!")
        oyuncuSkor += 1
    elif oyuncu == "Kağıt" and bilgisayar == "Taş":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Tebrikler")
        oyuncuSkor += 1
    elif oyuncu == "Makas" and bilgisayar == "Taş":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Puan Bilgisayarın")
        bilgisayarSkor += 1
    elif oyuncu == "Kağıt" and bilgisayar == "Makas":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Puan Bilgisayarın")
        bilgisayarSkor += 1
    elif oyuncu == "Taş" and bilgisayar == "Kağıt":
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Puan Bilgisayarın")
        bilgisayarSkor += 1
    elif oyuncu == bilgisayar:
        print("Bilgisayarın Hamlesi:", bilgisayar)
        print("Berabere")

if bilgisayarSkor > oyuncuSkor:
    print("Bilgisayarın Toplam Puanı:", bilgisayarSkor, "Senin Toplam Puanın:", oyuncuSkor)
    print("KAYBETTİNİZ")
elif bilgisayarSkor < oyuncuSkor:
    print("Bilgisayarın Toplam Puanı:", bilgisayarSkor, "Senin Toplam Puanın:", oyuncuSkor)
    print("MÜKEMMEL KAZANDINIZZZZ!")
else:
    print("Bilgisayarın Toplam Puanı:", bilgisayarSkor, "Senin Toplam Puanın:", oyuncuSkor)
    print("OYUN BERABERE BİTTİ")
print('Hoşgeldiniz')

sayi1 = int(input("Lütfen ilk  sayıyı giriniz : "))

sayi2 = int(input("Lütfen ikinci sayıyı  giriniz : "))

toplam = 0


while sayi1 <= sayi2 :
    toplam += sayi1
    sayi1 += 1

print("Girdiğiniz sayıların toplamı :", toplam)


boy = float(input(" Lütfen Boyunuzu giriniz : "))
agirlik = float(input("Lütfen ağırlığınızı giriniz : "))


vki = agirlik / (boy * boy)


if 18 <= vki < 25:
    durum = "Normal"
    print('Normal')
elif 25 >= vki < 30:
    durum = "Kilolu"
    print('kilolu')
elif 30 <= vki:
    durum = "Obez"
    print('Obez')
else: vki >= 35
durum = "Aşırı Obez"
print('Aşırı Obez')

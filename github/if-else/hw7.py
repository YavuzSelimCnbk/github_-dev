print('Merhaba')

islemci_türü= input("İşlemci türünü giriniz : ")
bilgisayar_ram = int(input("Ramini  giriniz (gb) : "))


if islemci_türü >= "i7" or bilgisayar_ram >= 8:
    print("Kuruluma uygundur.")
else:
    print("Kuruluma uygun değildir.") 
ifade = str(input('Lütfen bir ifade giriniz : '))

harf = str(input('Lütfen bir harf giriniz : '))

toplam = 0

for example in ifade :
  if example == 'a':
    toplam = toplam +1

    print('Bu metinde "a" harfinden toplam :',toplam,'tane vardır')
note1 = float(input('Birinci notunuzu giriniz : '))

note2 = float(input('İkinci notunuzu giriniz : ')) 

note3 = float(input('Performans notunuzu giriniz : '))

average = (note1 + note2 + note3 / 3)

if average >= 50 :
    print('Başarılı')

else :
    print('Başarısız')
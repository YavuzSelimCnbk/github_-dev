angle1 = int(input('Birinci açıyı giriniz : '))

angle2 = int(input('İkinci açıyı giriniz : ')) 

angle3 = int(input('Üçüncü iç açıyı giriniz : ')) 

average = (angle1 + angle2 + angle3)

triangel = 180

if average == triangel :
    print('Bu bir üçgendir.')

else :
    print('Bu bir üçgen değildir.')
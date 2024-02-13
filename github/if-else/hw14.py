number1 = int(input('Birinci sayıyı giriniz :'))
number2 = int(input('İkinci sayıyı giriniz :'))
number3 = int(input('Üçüncü sayıyı giriniz :'))
if number1 > number2 > number3 :
    print(number1)

elif number2 > number3 > number1 :
    print(number2)


elif number3 > number1 > number2 :
    print(number3)
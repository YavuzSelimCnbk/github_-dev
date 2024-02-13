
luggage = int(input('Lütfen kullandığınız bahaj hakkını giriniz (KG) : '))

if luggage <= 20 :
    print('Herhangi bir ücret ödemenize gerek yok.')

elif luggage > 20 : 

 additional_luggage = luggage - 20

 fee = additional_luggage * 10

 print('Ödemeniz gereken tutar : ',fee)
     
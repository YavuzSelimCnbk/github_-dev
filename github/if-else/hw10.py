price1 = 5
price2 = 4
price3 = 3 

time = float(input('Otoparkta kaldığınız süreyi giriniz :'))
           
if time <= 1.00 :
 print('Ödemeniz gereken ücret :' , price1 * time)

elif time > 1.00 and time <= 5.00 :
 print('Ödemeniz gereken ücret :' , price2 * time)

elif time > 5.00 :
 print('Ödemeniz gereken ücret :', price3 * time) 
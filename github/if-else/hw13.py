name = str(input('Adınızı giriniz :'))

wage = float(input('Maaşınızı giriniz :'))

working_years = int(input('Çalıştığınız yılı giriniz :'))


if working_years <= 5 :
   
   raised_wage = (wage * 1.10)

   print('Sayın', name , 'Zamlı maaşınız :', raised_wage)

elif working_years > 6 and working_years <= 10 :
 raised_wage = (wage * 1.15)

 print('Sayın', name , 'Zamlı maaşınız :', raised_wage)


elif working_years > 10 :
  raised_wage = (wage * 1.25)


  print('Sayın', name , 'Zamlı maaşınız :', raised_wage)

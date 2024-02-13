while True :

 password = input('Lütfen 8 karakterli bir şifre giriniz : ')

 if len(password) < 8 or len(password) >8 :
      print (input('Lütfen 8 Karakterli şifre giriniz : '))

 elif  len(password) == 8 :
  print('Şifreniz Kaydedildi')
  break

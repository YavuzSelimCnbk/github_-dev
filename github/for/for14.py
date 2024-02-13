import random 
loop = True

while loop :

 guess = int(input('Lütfen 0-20 arasında bir tahminde bulunun : '))

 
 if guess == 19 :
    print('Doğru sonuca ulaştınız ')


 elif guess <= 19 :
   print('Arttır !')
 

 elif guess >= 19 :
    print('Azalt !')
  


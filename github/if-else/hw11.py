angle1 = int(input('1. iç açıyı giriniz : '))

angle2 = int(input('2. iç açıyı giriniz : ')) 

angle3 = int(input('3. iç açıyı giriniz : '))

if angle1 == angle2 or angle2 == angle3 :

 print('Bu bir ikizkenar üçgendir.')

elif angle1 == angle2 == angle3 :
 print('Bu bir eşkenar üçgendir.')

elif angle1!= angle2!= angle3 : 

   print('Bu bir çeşitkenar üçgendir.')

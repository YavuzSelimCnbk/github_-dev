def getweek():
 week = int(input("Yurtda kaç hafta kaldığınızı giriniz : "))
 return week


def gethours(week):
 toplam = 0
 for i in range(week):
    hours = int(input(f"{i+1}. haftada kaç saat dini ders yaptığınızı giriniz : "))
    toplam += hours 
 return toplam
    
def islemal():
 process = str(input("Toplam mı almak istersiniz Ortalama mı (T/O) :"))
 return process

def islemyazdır(week,toplam , process):

 if process == "T" or process == "t" : 
  print(toplam)

 elif process == "O" or process == "o" :
  print(toplam / week)


x = getweek()

y = gethours(x)

z = islemal()

islemyazdır(x,y,z)



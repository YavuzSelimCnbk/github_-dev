def getnumbers():
 numbers = input("Listeye almak istediğiniz sayıları boşluklar ile giriniz : ")
 return numbers

def printlist(numbers):
 list = numbers.split(" ")
 print(f"Liste : {list}")

x = getnumbers()

printlist(x)


"""Girilen sayıları listeye alan kod bloğu"""
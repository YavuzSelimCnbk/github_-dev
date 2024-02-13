from math import pi

def getr():
 r = float(input("Dairenin r'sini giriniz :"))
 return r

def process(r):
 area = pi * r **2
 print(area)


x = getr()
process(x)

"""Kullanıcıdan alınan r ile dairenin alanını bulan kod bloğu"""
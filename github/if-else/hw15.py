
tercih = input("İzlemek istediğiniz türü seçiniz , sinema(S) , Tiyatro(T) : ")
ogrenci = input("Öğrenci misiniz Evet(E) hayır(H : ")

if tercih == 'S' or 's' and ogrenci == 'E' or 'e':
    ucret = 15 * 0.5  
elif tercih == 'S' or 's' and ogrenci == 'H' or 'h':
    ucret = 15
elif tercih == "T" or 't' and ogrenci == "E" or 'e':
    ucret = 10 * 0.5 
elif tercih == "T" or 't' and ogrenci == "H" or 'h':
    ucret = 10
else:
    ucret = 0  


if ucret > 0:
    print(input(ucret)("Ödemeniz gereken ücret:  TL"))
else:
    print("Yanlış tercih girdiniz veya yanlış tuşa bastınız.")





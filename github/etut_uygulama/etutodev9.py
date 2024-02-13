def generate_fibonacci_sum(limit):

    ilksayi = 1
    ikincisayi = 2
    toplam = 0

    if ilksayi % 2 == 0:
        toplam += ilksayi
    if ikincisayi % 2 == 0:
        toplam += ikincisayi

    if ikincisayi <= limit :
        digersayi = ilksayi + ikincisayi
        if digersayi % 2 == 0:
            toplam += digersayi

    ilksayi = digersayi
    ikincisayi = digersayi 
    return toplam

sonsayi = 4000000

sonuc = generate_fibonacci_sum(sonsayi)

print(sonuc)

####
""""""

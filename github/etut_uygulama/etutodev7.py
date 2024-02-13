def primenumber(number):

    
    for i in range(2,number):
        if number % i == 0 :
           return False
    return True
        
for i in range(100):
    if primenumber(i):
     print(i)

"""1'den 100'e kadar olan sayıların asal olanları yazdıran kod bloğu"""
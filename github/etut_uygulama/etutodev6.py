def getlist():
    list = [1,7,10,34,2,8]
    return list

def getlargestnumber(list):
    
    largenumber = list[0]

    for i in list :
        if i >= largenumber :
            largenumber = i
    print(largenumber)
        


x = getlist()
getlargestnumber(x)


"""Listedeki en büyük sayıyı bulan kod bloğu"""
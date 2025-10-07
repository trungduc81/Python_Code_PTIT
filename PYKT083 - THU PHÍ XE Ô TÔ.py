def count(loaiXe , soGhe):
    if loaiXe == "Xe_con":
        if soGhe == '5' : return 10000
        else : return 15000
    elif loaiXe == "Xe_tai" :
        return 20000
    else :
        if soGhe == '29' : return 50000
        else : return 70000

n = int(input())
dict = {}
for i in range(n) :
    tmp = input().split()
    if tmp[3] == "IN" :
        if tmp[4] not in dict:
            dict[tmp[4]] = count(tmp[1] ,  tmp[2])
        else :
            dict[tmp[4]] += count(tmp[1] , tmp[2])
for ngay , tong_tien in dict.items():
    print( str(ngay) + ": " + str(tong_tien))



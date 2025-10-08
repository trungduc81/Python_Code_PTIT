class SinhVien :
    def __init__(self,ma,ten,lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.cc = 10
        self.ghichu = ""
    def diem_cc(self,s):
        self.cc -= s.count("m")
        self.cc -= 2* s.count("v")
        if self.cc < 0 : self.cc = 0
        if self.cc == 0 :
            self.ghichu = "KDDK"
    def __str__(self):
        if self.ghichu:
            return f"{self.ma} {self.ten} {self.lop} {self.cc} {self.ghichu}"
        else :
            return f"{self.ma} {self.ten} {self.lop} {self.cc}"

n = int(input())
ds = []

for i in range(n):
    ma = input().strip()
    ten = input().strip()
    lop = input().strip()
    ds.append(SinhVien(ma, ten, lop))

for i in range(n):
    ma , s = input().split()
    for sv in ds :
        if sv.ma == ma :
            sv.diem_cc(s)
            break
for sv in ds :
    print(sv)


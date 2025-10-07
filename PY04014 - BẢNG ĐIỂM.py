class HocSinh :
    def __init__(self,ma,hoTen,diem):
        self.ma = ma
        self.hoTen = hoTen
        self.diem = diem
        self.diemTB = self.dtb()
        self.xepLoai = self.xep_loai()

    def dtb(self):
        tong = self.diem[0]*2 + self.diem[1]*2 + sum(self.diem[2:])
        return round(tong/12+1e-8,1)

    def xep_loai(self):
        if self.diemTB >= 9 :
            return "XUAT SAC"
        elif 8 <= self.diemTB < 9 :
            return "GIOI"
        elif 7 <= self.diemTB < 8 :
            return "KHA"
        elif 5 <= self.diemTB < 7 :
            return "TB"
        else : return "YEU"

    def __str__(self):
        return f"{self.ma} {self.hoTen} {self.diemTB:.1f} {self.xepLoai}"

n = int(input())
ds = []
for i in range(1,n+1):
    ten = input()
    diem = list(map(float , input().split()))
    ma = f"HS{i:02d}"
    ds.append(HocSinh(ma,ten,diem))
ds = sorted(ds,key = lambda x: (-x.diemTB , x.ma ))
for i in ds:
    print(i)





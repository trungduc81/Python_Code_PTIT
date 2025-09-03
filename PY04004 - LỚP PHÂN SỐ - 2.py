import math
class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toigian(self):
        ucln = math.gcd(self.tu , self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return self
    def tong(self,x,y):
        self.tu = x.tu * y.mau + x.mau * y.tu
        self.mau = x.mau * y.mau
        return self.toigian()

a , b , c ,d  = map(int , input().split())
p1 = PhanSo(a,b)
p2 = PhanSo(c,d)
tmp = PhanSo(1,2)
res = tmp.tong(p1,p2)
print(res.tu , res.mau , sep = "/")

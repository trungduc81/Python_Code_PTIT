import math
class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toigian(self):
        ucln = math.gcd(self.tu , self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return f"{self.tu}/{self.mau}"
a , b = map(int , input().split())
res = PhanSo(a,b)
res.toigian()
print(res)

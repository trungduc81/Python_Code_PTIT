class Rectangle:
    def __init__(self , dai , rong , color):
        self.dai = dai
        self.rong = rong
        self.color = color
    def check(self):
        if self.dai <=0 or self.rong <= 0: return False
        return True 
    def __str__(self):
        return f"{(self.dai + self.rong)*2} {self.dai * self.rong} {self.color.title()}"
a = input().split()
r = Rectangle(int(a[0]) , int(a[1]) , a[2])
if r.check(): print(r)
else : print("INVALID")

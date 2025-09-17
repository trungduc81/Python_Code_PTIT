import math
from decimal import Decimal
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self , p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx**2 + dy**2)
class Triangle:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        a , b, c = self.x , self.y , self.z
        if a+b <= c or b+c <= a or c+a <= b :
            return f'INVALID'
        else : return f'{(math.sqrt(((a+b+c)*(a+b-c)*(c+a-b)*(-a+c+b)))/4):.2f}'

if __name__ == '__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for _ in range(t):
        p1 , p2 , p3 = Point(a[i] , a[i+1]) , Point(a[i+2] , a[i+3]) , Point(a[i+4] , a[i+5])
        d1 , d2 , d3 = p1.distance(p2) , p2.distance(p3) , p3.distance(p1)
        res = Triangle(d1,d2,d3)
        print(res)
        i += 6

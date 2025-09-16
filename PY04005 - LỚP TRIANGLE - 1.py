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
        if self.x + self.y <= self.z or self.x + self.z <= self.y or self.y + self.z <= self.x :
            return f'INVALID'
        else : return f'{(self.x + self.y + self.z):.3f}'

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






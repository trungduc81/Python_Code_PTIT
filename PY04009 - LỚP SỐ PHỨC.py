for _ in range(int(input())):
    a , b , c , d = map(int , input().split())
    x1 , x2 = complex(a,b) , complex(c,d)
    res1 = (x1+x2) * x1
    res2 =(x1+x2) * (x1+x2)
    print(f"{int(res1.real)} + {int(res1.imag)}i",end = ", ")
    print(f"{int(res2.real)} + {int(res2.imag)}i")




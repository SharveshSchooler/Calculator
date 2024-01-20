def add(a,b,c):
    if c=="+":
      z=a+b
      return z
def sub(a,b,c):
    if c=="-":
     z= a-b
     return z
def mul(a,b,c):
    if c=="*":
     return a*b
def div(a,b,c):
    if c=="/":
     z= a/b
     return z
def sqroot(a,b,c):
    while c=="r":
        f=input("Press a or b")
        if f=="a":
            return (a)**0.5
        elif f=="b":
            return (b)**0.5
def sq(a,b,c):
    while c=="2**":
        m=input("Press a or b")
        if m=="a":
            return (a)**2
        elif m=="b":
            return (b)**2
        else:
            return
def binary(a,b,c):
    if c=="b":
        m=input("press a or b")
        if m=="a":
            g=""
            while a>0:
                b=a%2
                g=str(b)+g
                a= a//2
            return g
        elif m=="b":
            s=""
            while b>0:
                r=b%2
                s=str(r)+s
                b=b//2
            return s
def cubic(a,b,c):
    if c=="3":
        h= input("Enter a or b :")
        if h=="a":
            u= a**0.33333333333333333
            return u
        elif h=="b":
            e= b**0.33333333333333333
            return e
def vec(a,b,c):
    if c=="v":
        h= input( "Enter a^b or b^a")
        if h=="a^b":
            g=a**1/b
            return g
        elif h=="b^a":
            t=b**1/a
            return t
a=int(input("Enter a Number for a :"))
b=int(input("Enter a Number for b :"))
c=input("Press,+,-,*,/, r = sq Root,2**, b = Binary numbers , 3 = Cubic root,v = vector :")
if c=="+":
 print(add(a,b,c))
elif c=="-":
 print(sub(a,b,c))
elif c=="*":
  print(mul(a,b,c))
elif c=="/":
 print(div(a,b,c))
elif c=="r":
 print(sqroot(a,b,c))
elif c=="2**":
 print(sq(a,b,c))
elif c=="b":
 print(binary(a,b,c))
elif c=="3":
 print(cubic(a,b,c))
elif c=="v":
 print(vec(a,b,c))
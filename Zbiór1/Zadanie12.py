import time

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

print(nwd(nwd(a,b),c))
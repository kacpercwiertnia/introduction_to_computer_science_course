def fibbonaci(a,b):
  if abs( b/a - (a+b)/b ) < 0.000001:
    return b/a
  return fibbonaci(b,a+b)

a=int(input("a="))
b=int(input("b="))

print(fibbonaci(a,b))
def fibbonaci(a,b,c):
  if a*b>c:
    return False
  if a*b==c:
    return True
  return fibbonaci(b,a+b,c)

c=int(input("c="))

print(fibbonaci(1,1,c))
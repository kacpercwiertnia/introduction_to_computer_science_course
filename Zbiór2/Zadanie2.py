a=int(input("a="))
b=int(input("b="))
n=int(input("n="))

print(a//b,end=".")
while n>0:
  a*=10
  c = a//b
  a = a - c*b
  n-=1
  print(c,end="")
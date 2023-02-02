import math

a=int(input("a="))

print(1)

b = 2

while b <= a/2:
  if a%b==0:
    print(b)
  b+=1

print(a)
an=int(input("a1="))
bn=int(input("b1="))

while abs(an - bn) > 0.0000001:
  a1 = an
  b1 = bn
  an = (a1*b1)**(1/2)
  bn = (a1+b1)/2

print(an)
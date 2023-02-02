a=0
c=0
b = (1/2)**(1/2)
d = b

while abs(d-c) > 0.0001:
  a = b
  b = ((1/2)+(1/2)*a)**(1/2)
  c = d
  d *= b

print(2/d)

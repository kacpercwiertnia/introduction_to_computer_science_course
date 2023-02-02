a=-1
b=5

while abs(a-b) > 0.0001:
  x = (a+b)/2

  if abs(x**x-2020) <= 0.0001:
    break
  elif (x**x-2020) * (a**a-2020) < 0:
    b = x
  else:
    a = x

print((a + b) / 2)
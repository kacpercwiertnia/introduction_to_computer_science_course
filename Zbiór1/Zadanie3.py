a = 1
b = 1
suma = 0 

c = int(input("c="))

while suma < c:
  suma += a
  tmp = b
  b = a+b
  a = tmp

if suma == c:
  print("istnieje")

else:
  a = 1
  b = 1
  while suma > c:
    suma -= a
    tmp = b
    b = a+b
    a = tmp
  
  if suma == c:
    print("istnieje")
  else:
    print("nie istnieje")
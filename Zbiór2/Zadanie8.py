n = int(input("n="))

suma = n

while n==suma:
  n+=1
  a = 1
  b = 1
  suma = 0

  while suma < n:
    suma += a
    a , b = b, a+b

  a = 1
  b = 1

  while suma > n:
    suma -= a
    a , b = b, a+b

print(n)
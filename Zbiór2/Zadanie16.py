def licz_suma_cyfr(n):
  suma = 0
  while n > 0:
    suma += n%10
    n//=10
  return suma

def czy_smith(n):
  suma_cyfr_dziel = 0
  tmp = 0
  suma_cyfr = licz_suma_cyfr(n)
  for dziel in range(2, n//2 + 1):
    if n % dziel == 0:
      tmp = licz_suma_cyfr(dziel)
      while n % dziel == 0:
        suma_cyfr_dziel += tmp
        n //= dziel

  return suma_cyfr == suma_cyfr_dziel

for i in range(1,1000001):
  if czy_smith(i):
    print(i)
def dlugosc(n):
  dl = 0
  while n > 0:
    dl+=1
    n//=10
  
  return dl


def generuj_liczbe(n, i):
  nowa_tmp = 0
  while n > 0:
    if i % 2 == 1:
      nowa_tmp *= 10
      nowa_tmp += n % 10
    i //= 2
    n //= 10
  
  nowa = 0
  while nowa_tmp > 0:
    nowa *= 10
    nowa += nowa_tmp % 10
    nowa_tmp //= 10

  return nowa

n = int(input("n="))

ilosc = 0
for i in range(1, 2**dlugosc(n)):
    if generuj_liczbe(n, i) % 7 == 0:
        ilosc += 1

print(ilosc)
def czy_doskonala(a):
  if a%2!=0:
    return False
  
  suma = 1
  dzielnik = 2

  while dzielnik**2<a:
    if a%dzielnik==0:
      suma+=dzielnik+a/dzielnik
    dzielnik+=1

  if suma==a:
    return True
  
  return False

a=2

while a<1000001:
  if czy_doskonala(a):
    print(a)
  a+=2
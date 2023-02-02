def czy_pierwsza(n):
  if n < 2:
    return False
  if n == 2 or n == 3:
    return True
  if n % 2 == 0:
    return False
  
  dzielnik = 3

  while dzielnik*dzielnik <= n:
    if n%dzielnik == 0:
      return False
    dzielnik+=2
  
  return True
#end def

def wypisywanie(n, wynik = 0, poz = 0, warunek = False):
  if n == 0:
#    print(wynik)
    if wynik > 9 and czy_pierwsza(wynik) and warunek:
      print(wynik)
    return
  wypisywanie(n//10,wynik,poz,True)
  wypisywanie(n//10,wynik + ((n%10)*10**poz),poz+1,warunek)


wypisywanie(1234)
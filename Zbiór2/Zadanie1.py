def fibbonaci(a):
  x = 1
  y = 1
  while x < a:
    tmp = y
    y = x+y
    x = tmp
  
  if x == a:
    return True
  
  return False

def czy_iloczyn(a):
  
  if a==1:
    return True
  
  dzielnik = 1

  while a > dzielnik*dzielnik:
    if a%dzielnik == 0:
      if fibbonaci(dzielnik) and fibbonaci(a//dzielnik):
        return True
    dzielnik+=1
  
  return False

a=int(input("a="))

print(czy_iloczyn(a))
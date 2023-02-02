def dwa_trzy_piec(n):
  for dzielnik in {2,3,5}:
    while n%dzielnik==0:
      n//=dzielnik
  
  if n == 1:
    return True
  
  return False

n=int(input("n="))

ilosc = 0

for i in range(1,n+1):
  if dwa_trzy_piec(i):
    ilosc+=1

print(ilosc)
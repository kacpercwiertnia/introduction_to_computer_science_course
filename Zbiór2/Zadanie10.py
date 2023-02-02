def czy_wiel(n):
  an = 2
  while an <= n:
    if n%an == 0:
      return True
    an = 3*an + 1
  
  return False

n=int(input("n="))

print(czy_wiel(n))



def czy_wiel(n):
  i = 1
  ai = 0
  while ai <= n:
    ai = i*i+i+1
    if n%ai==0:
      return True
    i+=1
  
  return False

n = int(input("n="))

print(czy_wiel(n))

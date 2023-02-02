def czy_rosnacy(n):
  while n > 0:
    cyfra = n%10
    n//=10
    if cyfra <= n%10:
      return False
  
  return True

n = int(input("n="))

print(czy_rosnacy(n))
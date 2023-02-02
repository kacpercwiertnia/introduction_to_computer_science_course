def czy_unikalna(n):
  cyfra = n%10
  n//= 10
  while n > 0:
    if cyfra == n%10:
      return False
    n//=10
  return True

n = int(input("n="))

print(czy_unikalna(n))
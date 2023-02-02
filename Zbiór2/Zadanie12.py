def czy_zawiera(n,d):
  while n > 0:
    cyfra = n%10

    if d == cyfra:
      return True
    
    n //= 10
  return False

def dl(n):
  d = 0
  while n > 0:
    d += 1
    n //= 10
  return d

n = int(input("n="))

print(czy_zawiera(n,dl(n)))


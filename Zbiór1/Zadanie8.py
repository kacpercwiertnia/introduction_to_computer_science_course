import math

def czy_pierwsza(a):
  if a < 2:
    return False
  if a == 2 or a == 3:
    return True
  if a % 2 == 0 or a % 3 == 0:
    return False
  i = 5
  while i <= math.sqrt(a):
    if a % i == 0:
      return False
    i += 2
    if a % i == 0:
      return False
    i += 4
  return True

a = int(input("a="))

print(czy_pierwsza(a))

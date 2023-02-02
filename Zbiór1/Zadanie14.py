x=float(input("x="))
n=0
silnia=1
cosx1= 0
cosx2= 1

while abs(cosx1-cosx2) > 0.0001:
  cosx1 = cosx2
  n+=2
  silnia*=n*(n-1)
  if n%4==0:
    cosx2+=x**n/silnia
  else:
    cosx2-=x**n/silnia

print(cosx2)
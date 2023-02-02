def czy_ok(n,p):
  suma = 0
  tmp = n
  while tmp > 0:
    suma += (tmp%10)**p
    tmp//=10
  
  if n == suma:
    return True
  
  return False

n = int(input("n="))

start = 10**(n-1)

koniec=start*10

while start < koniec:
  if czy_ok(start,n):
    print(start)
  start+=1
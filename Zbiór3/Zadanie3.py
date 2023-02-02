n = int(input("n="))
liczby = [True for _ in range(n+1)]
podst = 2

while podst*podst <= n:
  if liczby[podst]!=False:
    wiel = podst
    while podst*wiel<=n:
      liczby[podst*wiel]=False
      wiel+=1
  podst+=1

for i in range(2,n+1):
  if liczby[i]:
    print(i)
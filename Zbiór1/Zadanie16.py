kroki_maks = 0
a1_maks = 0

for a1 in range(2,10001):
  an1 = a1
  kroki = 1
  while an1!=1:
    an1=(an1%2)*(3*an1+1)+(1-an1%2)*an1/2
    kroki+=1
  if kroki > kroki_maks:
    kroki_maks = kroki
    a1_maks = a1
  
print(a1_maks)
def fibbonaci(a,b):
  if( a+b > 2021 ):
    return b
  return fibbonaci(b,a+b)

naj_suma = 2021
naj_a = 0
naj_b = 0

for a in range(1, 2022):
  for b in range(1,2022-a):
    if fibbonaci(a,b)==2021:
      suma = a+b
      if suma < naj_suma:
        naj_suma = suma
        naj_a = a
        naj_b = b

print(naj_a,naj_b)
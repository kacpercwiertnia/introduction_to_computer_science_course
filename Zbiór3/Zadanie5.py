ciag = [0 for _ in range(10)]
tmp = [0 for _ in range(10)]
wejscie = 1

while wejscie != 0:
  index = -1
  wejscie = int(input("wyraz="))
  
  for i in range(10):
    if wejscie > ciag[i]:
      index+=1
    else:
      break

  if( index > -1 ):
    for i in range(1,index+1):
      tmp[i-1] = ciag[i]

    for i in range(index+1):
      ciag[i] = tmp[i]
    
    ciag[index] = wejscie

print(ciag[0])
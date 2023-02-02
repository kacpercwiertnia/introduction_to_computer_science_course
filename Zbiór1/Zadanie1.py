def fibbonaci(a,b):
  if( a+b > 1000000 ):
    return
  print(a+b)
  return fibbonaci(b,a+b)

fibbonaci(1,1)
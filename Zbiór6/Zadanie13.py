def P(n,s = 1, p=""):
  if n == 0 and len(p)>3:
    print(p)
    return
  else:
    for i in range(s,n+1):
      P(n-i,i,p+str(i)+" ")
    return

P(10)
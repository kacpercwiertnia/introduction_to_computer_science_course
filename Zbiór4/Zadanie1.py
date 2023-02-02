def na_system(n,s):
  liczba=[]
  alfabet=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  while n > 0:
    liczba.append(alfabet[n%s])
    n//=s
  return "".join(liczba[::-1])

n = int(input("n="))

for i in range(2,17):
  print(n,"w systemie:",i,":",na_system(n,i))

def rewers(a,s):
  liczba = 0
  while a > 0:
    c=a%s
    liczba*=s
    liczba+=c
    a//=s
  return liczba

a=int(input("a="))

print("palindrom dziesietny: ", rewers(a,10) == a)

print("palindrom dwojkowy:", rewers(a,2) == a)


def nww(a,b):
  if a > b:
    a,b=b,a
  if b%a==0:
    return b
  else:
    c = 2
    wielokrotnosc = 1
    while b > 1 and c <= b:
      if a%c==0 or b%c==0:
        wielokrotnosc*=c
        if a%c==0:
          a/=c
        if b%c==0:
          b/=c
      else:
        c+=1
    if b>1:
      wielokrotnosc*=c
    return wielokrotnosc
  
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

print(nww(nww(a,b),c))
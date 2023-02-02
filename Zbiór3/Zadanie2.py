cyferki = [0 for _ in range(10)]
a = int(input("a="))
b = int(input("b="))

while a!=0:
  cyferki[a%10]+=1
  a//=10

while b!=0:
  cyferki[b%10]-=1
  b//=10

for i in cyferki:
  if(i!=0):
    print("Nie są")
    break
else:
  print("Są")
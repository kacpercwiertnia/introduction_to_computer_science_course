k = int(input("k="))

pole = 0
x = 1

while k > x:
  pole += (1/x)*0.001
  x+=0.001

print(pole)

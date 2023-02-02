s=float(input("s="))

an = 1
an1 = 0

while abs(an - an1) > 0.0000001:
  an1 = an
  an = (s/(an*an) + 2*an)/3

print(an1)
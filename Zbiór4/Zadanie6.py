T1 = [[30,4,10],[9,8,6],[6,15,4]]
T2 = [0 for _ in range(len(T1)*len(T1))]

def singletony(T1,T2):
  for y in range(len(T1)):
    for x in range(len(T1)):
      z = len(T2)-1
      while T2[z] > T1[y][x]:
        z-=1
      if T2[z] == T1[y][x]:
        T2[z] = 0
      else:
        wcho = T1[y][x]
        while T2[z] != 0:
          wych = T2[z]
          T2[z]= wcho
          z-=1
          wcho = wych
        T2[z] = wcho
  return
#end def

singletony(T1,T2)
print(T2)
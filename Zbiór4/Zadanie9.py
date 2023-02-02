T = [[1,2,1,1,1],
     [2,1,1,2,1],
     [1,1,5,1,1],
     [1,2,1,1,1],
     [1,2,1,1,5]]

def kwadrat(T,k):
  bok = 2
  while bok < len(T):
    for y in range(len(T)-bok):
      for x in range(len(T)-bok):
        iloczyn = T[y][x] * T[y][x+bok] * T[y+bok][x] * T[y+bok][x+bok]

        print(T[y][x],T[y][x+bok],T[y+bok][x],T[y+bok][x+bok],iloczyn)
        print("")
        if k == iloczyn:
          print("istnieje: ",x+(bok//2), y+(bok//2))
          return
    bok +=2
  return


#end def

kwadrat(T,25)
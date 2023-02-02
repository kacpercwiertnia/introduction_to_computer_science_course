def zew(T,k):  
  def rek(T,k,koszt=T[k][0],kroki=0,x=0,y=k):
    Lewy = False
    Prawy = False
    if kroki == 7:
      return koszt
    
    if kroki < y:
      if x > 0:
        Lewy = True
      if x < 8:
        Prawy = True
    
    if y != 6 or kroki >= 6: 
      if Lewy:
        return min(rek(T,k,koszt+T[y][x-1],kroki+1,x-1,y), rek(T,k,koszt+T[y+1][x],kroki+1,x,y+1))
      elif Prawy:  
        return min(rek(T,k,koszt+T[y][x+1],kroki+1,x+1,y), rek(T,k,koszt+T[y+1][x],kroki+1,x,y+1))
      return rek(T,k,koszt+T[y+1][x],kroki+1,x,y+1)
    
    if Lewy:
      return rek(T,k,koszt+T[y][x-1],kroki+1,x-1,y)
    elif Prawy:
      return rek(T,k,koszt+T[y][x+1],kroki+1,x+1,y)
  return rek(T,3)

T = [[1,3,1,1,1,1,1,1],
     [1,15,1,1,1,1,1,1],
     [1,600,1,1,1,1,1,1],
     [1,3,600,1,1,1,1,1],
     [1,3,1,600,1,1,1,1],
     [1,1,1,1,600,1,1,1],
     [1,1,1,1,1,600,1,1],
     [1,1,1,1,1,1,1,1]]

print(zew(T,3))
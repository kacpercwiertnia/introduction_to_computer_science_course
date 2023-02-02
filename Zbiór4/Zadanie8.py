T = [[1,1,1,1,2],
     [1,2,1,1,1],
     [1,1,3,2,1],
     [1,3,2,8,2],
     [1,1,9,1,1]]

def sprawdzanie(T,x,y):
  maks_dl = 2
  dl = 1
  r = T[y][x] / T[y+1][x+1]
  while y < len(T)-1 and x < len(T)-1:
    next_r = T[y][x] / T[y+1][x+1]
    if next_r == r:
      dl += 1
      if maks_dl < dl:
        maks_dl = dl
    else:
      r = next_r
      dl = 2
    x+=1
    y+=1
  return maks_dl

def ciag(T):
  a = 0
  maks_dl = 2
  while a < len(T)-2:
    dl = sprawdzanie(T,0,a)
    if dl > maks_dl:
      maks_dl = dl
    dl = sprawdzanie(T,a,0)
    if dl > maks_dl:
      maks_dl = dl
    a+=1
  if maks_dl > 2: 
    print("Istnieje, dlugosc: ", maks_dl)

ciag(T)
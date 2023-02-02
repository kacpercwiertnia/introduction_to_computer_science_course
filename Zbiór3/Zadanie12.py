import random

n = int(input("n="))

tablica = [random.randrange(1,101,2) for _ in range(n)]

print(tablica)

dl_ros = 2
dl_mal = 2
dl_max_mal = 1
dl_max_ros = 1

if n > 1:
  r = tablica[0] - tablica[1]
  for i in range(1,n-1):
    if r == tablica[i] - tablica[i+1] and r > 0:
        dl_mal+=1
    else:
      r = tablica[i] - tablica[i+1]
      if dl_mal > dl_max_mal:
        dl_max_mal = dl_mal
        print(tablica[i])
      dl_mal = 2
  for i in range(1,n-1):
    if r == tablica[i] - tablica[i+1] and r < 0:
        dl_ros+=1
    else:
      r = tablica[i] - tablica[i+1]
      if dl_ros > dl_max_ros:
        dl_max_ros = dl_ros
        print(tablica[i])
      dl_ros = 2

print(dl_max_mal)
print(dl_max_ros)
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_growing(first):
  p = first

  if p is None or p.next is None:
    return first

  start = None
  stop = p
  start_maks = None
  stop_maks = None
  dl = 1
  flaga = False
  dl_maks = 0

  while p.next is not None:
    if p.val < p.next.val:
      dl+=1
      stop = p.next
    else:
      start = p
      stop = p.next
      dl = 1
    if dl >= dl_maks:
      if dl == dl_maks:
        flaga = True
      else:
        flaga = False
      dl_maks = dl
      start_maks = start
      stop_maks = stop
    p = p.next

  if not flaga:
    if start_maks is None:
      first = stop_maks.next
    else:
      start_maks.next = stop_maks.next

  return first

def print_linked_list(first):
  p = first

  while p is not None:
    print(' -->', p.val, end = '')
    p = p.next

  print()

def make_linked_list(tab):
  first = None
  n = len(tab)
  for i in range(n - 1, -1, -1):
    tmp = Node(tab[i])
    tmp.next = first
    first = tmp
  return first

t1 = [5,1,2,4,1]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_growing(first)
print_linked_list(first)
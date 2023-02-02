class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_more(key):
  suma = 0
  
  while key > 0:
    if key % 3 == 1:
      suma += 1
    elif key % 3 == 2:
      suma -= 1
    key //= 3
  
  if suma > 0:
    return True
  
  return False 

def pop_more(first):
  p = first
  q = None

  if p is None:
    return first

  while p is not None:
    if is_more(p.val):
      if q is not None:
        q.next = p.next
        p = p.next
      else:
        first = p.next
        p = first
    else:
      q = p
      p = p.next

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

t1 = [16,123,15,17]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_more(first)
print_linked_list(first)
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_five(key):
  suma = True
  
  while key > 0:
    if key % 8 == 5:
      suma = not suma
    key //= 8
  
  return suma

def five_front(first):
  p = first
  q = None

  if p is None or p.next is None:
    return first

  while p is not None:
    if is_five(p.val) and q is not None:
      s = first
      r = p
      p = p.next
      q.next = p
      first = r
      first.next = s
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

t1 = [7,45]
first = make_linked_list(t1)
print_linked_list(first)
first=five_front(first)
print_linked_list(first)
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def can_add(first,a):
  p = first

  if p is None:
    return True
  
  while p is not None:
    if p.val == a:
      return False
    if p.val < a:
      return True
    p = p.next

  return True

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

t1 = ["Ala","Ma","Kota"]
first = make_linked_list(t1)
print_linked_list(first)
print(can_add(first,"Kota"))
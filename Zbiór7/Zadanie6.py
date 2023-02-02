class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_to_end_linked_list(a,first):
  p = first
  q = None
  while p is not None:
    q = p
    p = p.next
    
  r = Node(a)
  
  q.next = r

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

t = [2, 3, 4, 5, 6, 8]
first = make_linked_list(t)
print_linked_list(first)
add_to_end_linked_list(9,first)
print_linked_list(first)
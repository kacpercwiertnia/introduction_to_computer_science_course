class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_by_key(first,key):
  p = first
  q = None

  if p is None:
    first = Node(key)
    return first

  if p.next is None:
    if p.val == key:
      p = None
    else:
      p.next = Node(key)
    return first

  while p is not None:
    if p.val == key:
      if q == None:
        first = p.next
      else:
        q.next = p.next
      return first
    q = p
    p = p.next

  q.next = Node(key)
      
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

t1 = []
first = make_linked_list(t1)
print_linked_list(first)
first=pop_by_key(first,2)
print_linked_list(first)
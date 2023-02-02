class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_lower(first):
  p = first
  q = None

  if p is None or p.next is None:
    return first

  while p.next is not None:
    if p.val < p.next.val:
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

t1 = [10,11]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_lower(first)
print_linked_list(first)
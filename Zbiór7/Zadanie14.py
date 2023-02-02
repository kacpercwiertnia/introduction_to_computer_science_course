class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_dividing(first):
  p = first
  q = None

  if p is None or p.next is None:
    return first

  while p.next is not None:
    if p.next.val % p.val == 0:
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

t1 = [2]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_dividing(first)
print_linked_list(first)
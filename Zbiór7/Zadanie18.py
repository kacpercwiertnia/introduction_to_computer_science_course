class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_dublets(first):
  r = first

  if r is None or r.next is None:
    return first

  while r is not None:
    p = r.next
    q = r
    while p is not None:
      if r.val == p.val:
        q.next = p.next
        p = p.next
      else:
        q = p
        p = p.next
    r = r.next

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

t1 = [1,1,5,1,5]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_dublets(first)
print_linked_list(first)
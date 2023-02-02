class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_from_end_linked_list(first):
  q = None
  p = first
  r = p.next
  while r.next is not None:
    q = p
    q.next = r.next
    p = r
    r = q.next
  p.next = None

  

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

t = [2, 3, 4, 5, 6, 8, 9]
first = make_linked_list(t)
print_linked_list(first)
pop_from_end_linked_list(first)
print_linked_list(first)
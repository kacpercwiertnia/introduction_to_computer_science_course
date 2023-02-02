class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def cicle_size(first):
  p = first

  if p is None or p.next is None:
    return False

  p_fast = first.next

  while p != p_fast:
    p = p.next
    p_fast = p_fast.next.next

  p_fast = p_fast.next
  size = 1

  while p != p_fast:
    p_fast = p_fast.next
    size+=1

  p = first
  p_fast = first

  for i in range(size):
    p_fast = p_fast.next
  
  q = None

  while p != p_fast:
    p_fast = p_fast.next
    q=p
    p = p.next

  return q.val

def print_linked_list(first):
  p = first

  while p is not None:
    print(' -->', p.val, end = '')
    p = p.next

  print()

def make_cycle(first):
  p = first

  while p.next is not None:
    p = p.next
  
  p.next = first.next.next.next

  return first

def make_linked_list(tab):
  first = None
  n = len(tab)
  for i in range(n - 1, -1, -1):
    tmp = Node(tab[i])
    tmp.next = first
    first = tmp

  return first

t1 = [5,1,3,1,2,3,5,6,7]
first = make_linked_list(t1)
print_linked_list(first)
first = make_cycle(first)
print(cicle_size(first))
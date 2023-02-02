class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_cicle(first):
  p = first

  if p is None or p.next is None:
    return False

  if p.next == p:
    return True
  
  p_fast = first.next

  while p_fast.next is not None and p_fast.next.next:
    if p == p_fast:
      return True
    p = p.next
    p_fast = p_fast.next.next

  return False

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
  
  p.next = first

  return first

def make_linked_list(tab):
  first = None
  n = len(tab)
  for i in range(n - 1, -1, -1):
    tmp = Node(tab[i])
    tmp.next = first
    first = tmp

  return first

t1 = [5,1,2,4,1,2,3,4,5]
first = make_linked_list(t1)
print_linked_list(first)
#first = make_cycle(first)
print(is_cicle(first))
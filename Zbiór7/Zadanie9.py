class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def increase_one(first):
  p = first

  if p is None:
    return first

  while p.next is not None and p.val == 9:
    p.val = 0
    p = p.next
  
  if p.val != 9:
    p.val += 1
  else:
    q = Node(1)
    p.val = 0
    p.next = q
  
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

t = [9, 9, 9, 9, 9, 8, 9]
first = make_linked_list(t)
print_linked_list(first)
increase_one(first)
print_linked_list(first)
first = None

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_in_linked_list(a):
  global first
  p = first
  while p is not None:
    if a == p.val:
      return True
    p = p.next
  return False

def add_to_linked_list(a):
  global first
  p = first
  q = None

  while p is not None and p.val < a:
    q = p
    p = p.next

  if p is not None and p.val == a:
    return
  
  r = Node(a)

  if q is not None:
    q.next = r
    r.next = p
  else:
    r.next = first
    first = r

def pop_from_linked_list(a):
  global first
  p = first
  q = None

  while p is not None and p.val < a:
    q = p
    p = p.next
  
  if p is None or p.val != a: 
    return
  
  if q is not None:
    q.next = p.next
  else:
    first = p.next


def print_linked_list():
  global first
  p = first

  while p is not None:
    print(' -->', p.val, end = '')
    p = p.next

  print()

def make_linked_list(tab):
  global first
  n = len(tab)
  for i in range(n - 1, -1, -1):
    tmp = Node(tab[i])
    tmp.next = first
    first = tmp
  return first

t = [2, 3, 4, 5, 6, 8]
first = make_linked_list(t)
print_linked_list()
print(is_in_linked_list(6))
add_to_linked_list(0)
print_linked_list()
pop_from_linked_list(4)
print_linked_list()
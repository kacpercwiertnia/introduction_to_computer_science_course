class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_two_lists(first,second):
  p = first
  q = second

  if p is None:
    return second
  elif q is None:
    return first
  
  r = Node(0)

  l = r

  while p is not None and q is not None:
    r.val += p.val + q.val
    if r.val > 9:
      r.next = Node(1)
      r.val -= 10
    elif p.next is not None or q.next is not None:
      r.next = Node(0)
    r = r.next
    p = p.next
    q = q.next

  if p is not None:
    s = p
  else:
    s = q
  
  while s is not None:
    r.val += s.val
    if r.val > 9:
      r.next = Node(1)
      r.val -= 10
    elif s.next is not None:
      r.next = Node(0)
    r = r.next
    s = s.next

  return l

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

t1 = [1,1]
first = make_linked_list(t1)
t2 = [1,1]
second = make_linked_list(t2)
print_linked_list(first)
print_linked_list(second)
print_linked_list(sum_two_lists(first,second))

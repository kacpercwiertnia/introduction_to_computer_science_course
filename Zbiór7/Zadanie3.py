class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

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

def merge_linked_lists_ite(first,second):
  p = first
  q = second
  
  if p.val < q.val:
    l = first
    p = p.next
  else:
    l = second
    q = q.next

  r = l

  while p is not None and q is not None:
    if p.val < q.val:
      r.next = p
      r = r.next
      p = p.next
    else:
      r.next = q
      r = r.next
      q = q.next

  while p is not None:
    r.next = p
    r = r.next
    p = p.next

  while q is not None:
    r.next = q
    r = r.next
    q = q.next

  return l

def merge_linked_lists_rek(first,second):
  p = first
  q = second
  if p == None:
    return q
  if q == None:
    return p
  
  if p.val <= q.val:
    r = p
    r.next = merge_linked_lists_rek(p.next,q)
  else:
    r = q
    r.next = merge_linked_lists_rek(p,q.next)
  
  return r

t = [2, 3, 4, 5, 6, 8]
t2 = [1, 2, 7, 9, 11, 20]
first = make_linked_list(t)
second = make_linked_list(t2)
print_linked_list(first)
print_linked_list(second)
print_linked_list(merge_linked_lists_ite(first,second))
#print_linked_list(merge_linked_lists_rek(first,second))
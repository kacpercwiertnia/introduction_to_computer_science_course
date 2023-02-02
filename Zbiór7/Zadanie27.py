class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_rek(first,second):
  p = first
  q = second

  if p is None:
    return q
  if q is None:
    return p

  if p.val <= q.val:
    r = p
    r.next=merge_rek(p.next,q)
  else:
    r = q
    r.next=merge_rek(p,q.next)
  
  return r
    

def merge_it(first,second):
  p = first
  q = second

  if p is None:
    return second
  if q is None:
    return first
  
  if p.val < q.val:
    r = p
    p = p.next
  else:
    r = q
    q = q.next

  l = r
  
  while p is not None and q is not None:
    if p.val < q.val:
      if p.val != r.val:
        r.next = p
        r = r.next
      p = p.next
    else:
      if q.val != r.val:
        r.next = q
        r = r.next
      q = q.next
  
  if p is not None:
    while p is not None:
      if p.val != r.val:
        r.next = p
        r = r.next
      p = p.next
  else:
    while q is not None:
      if q.val != r.val:
        r.next = q
        r = r.next
      q = q.next

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

t1 = [1,14]
t2 = [1,2,6,8,10,11,12,13,14]
first = make_linked_list(t1)
second = make_linked_list(t2)
print_linked_list(first)
print_linked_list(second)
first = merge_it(first,second)
print_linked_list(first)
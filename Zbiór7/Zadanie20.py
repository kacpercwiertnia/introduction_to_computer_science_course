class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_dublets(first):
  p = first

  if p is None or p.next is None:
    return first

  while p is not None:
    q = p.next
    r = q

    start = p.val[0]
    stop = p.val[1]

    while q is not None:
      if p.val[0] >= q.val[0] and p.val[0] <= q.val[1]:
        start = q.val[0]
        stop = max(p.val[1], q.val[1])
        if p.next == q:
          p.next = q.next
        r.next = q.next
        q = q.next
      elif p.val[0] <= q.val[0] and p.val[1] >= q.val[0]:
        start = p.val[0]
        stop = max(p.val[1], q.val[1])
        if p.next == q:
          p.next = q.next
        r.next = q.next
        q = q.next
      else:
        r = q
        q = q.next

    if p.val != (start,stop):
      p.val = (start,stop)
    else:
      p=p.next

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

t1 = [(2,9),(2,6)]
first = make_linked_list(t1)
print_linked_list(first)
first=pop_dublets(first)
print_linked_list(first)
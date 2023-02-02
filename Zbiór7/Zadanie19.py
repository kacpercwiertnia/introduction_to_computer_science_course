class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def pop_dublets(first):
  p = first
  poped = 0

  if p is None or p.next is None:
    return poped

  q = p.next

  while q is not None:
    if p.val == q.val:
      poped+=1
      q = q.next
    else:
      p.next = q
      p = q
      q = q.next
  
  if p.next is not q:
    p.next = None

  return poped

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

t1 = [1,1,2,2,3]
first = make_linked_list(t1)
print_linked_list(first)
print(pop_dublets(first))
print_linked_list(first)
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_in(first,second):
  p = first
  q = second

  if p is None:
    return False
  
  if p is not None and q is None:
    return True

  while p is not None and p != q:
    p=p.next
  
  if p is None:
    return False

  while q is not None and p is not None:
    if q != p:
      return False
    p = p.next
    q = q.next
  
  if p is None:
    if q is None:
      return True
    return False
  
  return True

  
  
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

def make_in_linked(first):

  for i in range(1):
    a = Node(i)
    a.next = first
    first = a
  
  p = first

  while p.next is not None:
    p=p.next
  
  for i in range(0):
    a = Node(i)
    p.next = a
    p=p.next
  
  return first



t1 = [5,1,3,1,2,3,5,6,7]
first = make_linked_list(t1)
second = make_in_linked(first)
print_linked_list(first)
print_linked_list(second)
print(is_in(first,second))
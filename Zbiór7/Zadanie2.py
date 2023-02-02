first = None

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def print_linked_list():
  global first
  p = first

  while p is not None:
    print(' -->', p.val, end = '')
    p = p.next

  print()

def index_value(a):
  global first
  p = first
  b = 0
  
  while p is not None:
    if b == a:
      return p.val
    b+=1
    p = p.next

  return

def change_index_value(a,b):
  global first
  p = first
  c = 0

  while p is not None:
    if c == a:
      p.val = b
      return
    c+=1
    p = p.next
  
  return

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
print(index_value(5))
change_index_value(0,10)
print_linked_list()
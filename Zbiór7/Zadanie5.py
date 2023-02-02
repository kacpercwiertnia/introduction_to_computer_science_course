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

def split_to_ten_list(first):
  ten_list = [None,None,None,None,None,None,None,None,None,None]
  ten_start = [None,None,None,None,None,None,None,None,None,None]
  p = first
  while p is not None:
    dig = p.val%10
    if ten_list[dig] is None:
      ten_list[dig] = p
      ten_start[dig] = ten_list[dig]
    else:
      ten_list[dig].next = p
      ten_list[dig] = p
    p = p.next
  for i in range(10):
    ten_list[i].next = None
    print_linked_list(ten_start[i])
  result = None
  for i in range(9,-1,-1):
    if ten_start[i] is not None:
      ten_list[i].next = result
      result = ten_start[i]
  print_linked_list(result)
  


def make_linked_list(tab):
  first = None
  n = len(tab)
  for i in range(n - 1, -1, -1):
    tmp = Node(tab[i])
    tmp.next = first
    first = tmp
  return first

t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
first = make_linked_list(t)
print_linked_list(first)
split_to_ten_list(first)

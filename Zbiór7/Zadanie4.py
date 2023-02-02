class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_linked_list(first):
    while first is not None:
        print(' -->', first.val, end = '')
        first = first.next


def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        tmp = Node(tab[i])
        tmp.next = first
        first = tmp
    return first

def reverse_linked_list(first):  
  if first is None or first.next is None:
    return first
  else:
    f = first
    s = first.next
    first.next = None
    while s.next is not None:
      t = s.next
      s.next = f
      f = s
      s = t
      t = t.next
    s.next = f
    first = s
    return first

t = [1, 2, 3, 4, 5, 6]
first = make_linked_list(t)
print_linked_list(first)
print()
first = reverse_linked_list(first)
print_linked_list(first)
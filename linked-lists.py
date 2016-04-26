#/usr/local/bin python3

# Given a Linked List where each node can be another linked list, write a 
# function that transforms that into a simple Linked List, flattening it. 

# What's the space and time complexity of your solution?

# Example input

# HEAD ---> ["hello"]--> ["world"]--> ["!"]--> null
#               |            |          |
#               |            |          |
#               v            v          v
#           ["brave"]       null       null
#               |
#               |
#               v
#            ["new"]
#               |
#               |
#               v
#              null

# Example Output

# HEAD ---> ["hello"]--> ["brave"]--> ["new"]--> ["world"]--> ["!"]--> null

class Node():
    def __init__(self, value):
        self.next = None
        self.below = None
        self.value = value

def print_flat_list(head):
    while head != None:
        print('[', head.value, ']', end='')
        if head.next != None:
            print(' --> ', end='')
        else:
            print(' --> null')
        head = head.next

def flatten_list(head):
    if not head:
        return None
    curr = head
    while curr != None:
        if curr.below != None:
            flatten(curr, curr.next)
        curr = curr.next
    return head

def flatten(head, next_node):
    while head.below != None:
        head.next = head.below
        head.below = None
        head = head.next
    head.next = next_node

test_input = Node('hello')
test_input.below = Node('brave')
test_input.below.below = Node('new')

test_input.next = Node('world')
test_input.next.next = Node('!')

flatten_list(test_input)
print_flat_list(test_input)
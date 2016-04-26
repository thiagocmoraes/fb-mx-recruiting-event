#/usr/local/bin python3

class Node():
    def __init__(self, value):
        self.next = None
        self.below = None
        self.value = value

def print_flat_list(head):
    while head != None:
        print(head.value, end='')
        if head.next != None:
            print(' --> ', end='')
        else:
            print(' --> null')
        head = head.next

foo = MyList('hola')
foo.next = MyList('mundo')
foo.next.next = MyList('!')

print_flat_list(foo)

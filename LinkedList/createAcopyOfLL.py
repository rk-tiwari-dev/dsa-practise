class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()
    
def copyLL(head):
    if head is None:
        return None
    new_head = node(head.data)
    new_head.next = copyLL(head.next)
    return new_head

# driver code            
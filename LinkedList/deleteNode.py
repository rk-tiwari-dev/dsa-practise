class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def deleteNode(head, key):
    if head is None:
        return None
    if head.data == key:
        return head.next
    current = head
    while current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next
    return head


def printLL(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()        
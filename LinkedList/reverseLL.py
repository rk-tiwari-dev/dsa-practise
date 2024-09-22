def reverseLL(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def printLL(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


printLL(reverseLL(Node(1)))
printLL(reverseLL(Node(1).next))
printLL(reverseLL(Node(1).next.next))
printLL(reverseLL(Node(1).next.next.next))

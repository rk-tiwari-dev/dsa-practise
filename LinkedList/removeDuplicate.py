def removeDuplicate(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# make LL of 1->1->2->3->3->4
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next.next = Node(6)


def printLL(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


printLL(removeDuplicate(head))  # 1 2 3 4 5 6

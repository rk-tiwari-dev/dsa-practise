def middletohead(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    slow.next = head
    head = slow
    return head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# make a LL of 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

printLL(middletohead(head))  # 4 1 2 3 5

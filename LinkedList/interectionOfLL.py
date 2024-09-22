class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insectionOfLL(head1, head2):
    if head1 is None or head2 is None:
        return None
    current1 = head1
    current2 = head2
    while current1 != current2:
        current1 = head2 if current1 is None else current1.next
        current2 = head1 if current2 is None else current2.next
    return current1


# make a LL of 1->2->3->4->5
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

# make a LL of 6->7->8->9->10
head2 = Node(6)         
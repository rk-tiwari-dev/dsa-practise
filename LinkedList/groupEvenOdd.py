class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def oddEvenLinkedList(head: ListNode) -> ListNode:
    if not head or not head.next:  # Edge case: Empty list or single node
        return head

    odd = head
    even = head.next  # Pointer for even-indexed nodes
    evenHead = even

    while even and even.next:
        odd.next = even.next  # Link odd nodes
        odd = odd.next
        even.next = odd.next  # Link even nodes
        even = even.next

    odd.next = evenHead  # Append even list after odd list
    return head


""" here we are using two pointers to keep track of odd and even nodes.\
    We are linking odd nodes and even nodes separately and then appending even list after odd list.\
    Time complexity: O(n) where n is the number of nodes in the linked list.\
    Space complexity: O(1) as we are using only constant space."""

def reverse_continuous_even_elements(head: ListNode) -> ListNode:
    if not head:
        return None
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    current = head

    while current:
        if current.val % 2 == 0:
            start = current
            while current and current.val % 2 == 0:
                current = current.next

            prev.next = reverseSublist(start, current)
            start.next = current
            prev = start
        else:
            prev = current
            current = current.next

    return dummy.next


def reverseSublist(start, end):
    prev = None
    current = start
    while current != end:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

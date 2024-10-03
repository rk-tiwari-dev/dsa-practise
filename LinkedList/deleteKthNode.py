class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_kth_from_end(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer k+1 steps ahead
    for _ in range(k + 1):
        first = first.next

    # Move first to the end, maintaining the gap
    while first is not None:
        first = first.next
        second = second.next

    # Remove the Kth node from the end
    second.next = second.next.next

    return dummy.next  # Return the head of the modified list

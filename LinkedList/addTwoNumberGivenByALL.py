from crio.ds.List.ListNode import *


def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Function to add two numbers represented by linked lists
def add(n1: ListNode, n2: ListNode) -> ListNode:
    # Step 1: Reverse both linked lists
    rev_head1 = reverseList(n1)
    rev_head2 = reverseList(n2)

    carry = 0
    result_head = None
    result_tail = None

    # Step 2: Add the numbers
    while rev_head1 or rev_head2 or carry:
        val1 = rev_head1.val if rev_head1 else 0
        val2 = rev_head2.val if rev_head2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        digit = total % 10

        # Create a new node with the sum of digits
        new_node = ListNode(digit)
        if not result_head:
            result_head = new_node
            result_tail = new_node
        else:
            result_tail.next = new_node
            result_tail = result_tail.next

        if rev_head1:
            rev_head1 = rev_head1.next
        if rev_head2:
            rev_head2 = rev_head2.next

    # Step 3: Reverse the result back to maintain the original order
    return reverseList(result_head)

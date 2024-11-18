class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: ListNode) -> ListNode:
    # Base case: if the list is empty or has a single element
    if not head or not head.next:
        return head

    # Split the list into two halves
    mid = get_middle(head)
    right_half = mid.next
    mid.next = None

    # Sort each half recursively
    left = sort_list(head)
    right = sort_list(right_half)

    # Merge the sorted halves
    return merge(left, right)


def get_middle(head: ListNode) -> ListNode:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append the remaining nodes of l1 or l2
    tail.next = l1 if l1 else l2

    return dummy.next

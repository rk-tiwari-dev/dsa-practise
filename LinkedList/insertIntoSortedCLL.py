def insertIntoSortedCircularList(head: ListNode, insertVal: int) -> ListNode:
    new_node = ListNode(insertVal)

    # Case 1: If the list is empty
    if not head:
        new_node.next = new_node  # New node points to itself, forming a circular list
        return new_node

    # Case 2: If the list contains one or more nodes
    prev, curr = head, head.next
    while True:
        # Case 2a: Inserting in the middle of the sorted list
        if prev.val <= insertVal <= curr.val:
            break

        if (
            prev.val > curr.val
        ):  # We are at the largest element transitioning to the smallest
            if insertVal >= prev.val or insertVal <= curr.val:
                break

        prev, curr = curr, curr.next

        # Case 2c: If we've come full circle (all values are equal)
        if prev == head:
            break

    # Insert the new node between `prev` and `curr`
    prev.next = new_node
    new_node.next = curr

    return head


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

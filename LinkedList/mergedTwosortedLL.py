# Problem Description
# Given 2 sorted linked lists, merge them into a new sorted linked list and return head of the merged list. The new list should be made by splicing (adjusting the pointers) together the nodes of the first two lists.

# Input format
# N - An integer denoting the number of nodes in the linked list.

# N integers follow where ith integer denotes the ith node value in the linked list

# M - An integer denoting the number of nodes in the linked list.

# M integers follow where jth integer denotes the jth node value in the linked list


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Return the sorted list after splicing the nodes of the first two lists.


def mergeTwoLists(l1, l2):
    dummy = node(0)
    head = dummy
    while l1 and l2:
        if l1.data < l2.data:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    if l1:
        head.next = l1
    if l2:
        head.next = l2
    return dummy.next


# driver code
l1 = node(1)
l1.next = node(2)
l1.next.next = node(4)
l1.next.next.next = node(5)


l2.next = node(1)
l2.next.next = node(3)
l2.next.next.next = node(4)
l2.next.next.next.next = node(6)
printLL(l1)
printLL(l2)

new_head = mergeTwoLists(l1, l2)
printLL(new_head)

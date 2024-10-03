# Given a linked list and an integer X, partition the LL around X, such that all nodes less than X come before all nodes greater than X.
# If X is contained within the list, then those nodes need

# to be after the elements less than X and before the elements greater than X,
# i.e. they should appear between the left and right partitions.


# You can also see if you can preserve the order for elements on either side of the partition. For instance, for given LL 2, 6, 5, 7, 1 and X = 5,
# the answer should be 2, 1, 5, 6, 7 only, instead of 1, 2, 5, 6, 7.

# The solution is to maintain two separate linked lists, one for elements less than X and one for elements greater than X.


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


def partition(head, x):
    smaller_head = smaller = node(0)
    greater_head = greater = node(0)

    while head:
        if head.data < x:
            smaller.next = head
            smaller = smaller.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next

    greater.next = None
    smaller.next = greater_head.next
    return smaller_head.next


# Driver code
head = node(3)
head.next = node(5)
head.next.next = node(8)
head.next.next.next = node(5)
head.next.next.next.next = node(10)
head.next.next.next.next.next = node(2)
head.next.next.next.next.next.next = node(1)
printLL(head)
x = 5
new_head = partition(head, x)
printLL(new_head)
# Output: 3 5 8 5 10 2 1
# 3 2 1 5 8 5 10

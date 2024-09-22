class Node: # class to create nodes of LL
    def __init__(self, value):
        self.value = value
        self.next = None
        
def printLL(head): # function to print the LL
    while head:
        print(head.value, end=" ")
        head = head.next
    print()
    
    
def checkCycle(head): # function to check if there is a cycle in LL or not
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# make a LL of 1->2->3->4->5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)            
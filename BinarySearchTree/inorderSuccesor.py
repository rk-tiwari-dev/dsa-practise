def inorderSuccessor(root: TreeNode, node: TreeNode) -> TreeNode:
    # Case 1: If the node has a right child, find the leftmost node in the right subtree
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    # Case 2: If the node has no right child, we need to find the successor by traversing the tree
    successor = None
    current = root

    while current:
        if node.val < current.val:
            # The node is in the left subtree
            successor = current
            current = current.left
        elif node.val > current.val:
            # The node is in the right subtree
            current = current.right
        else:
            # We've found the node, now break out of the loop
            break

    return successor

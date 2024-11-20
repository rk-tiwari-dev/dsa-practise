def kthLargestElementInABst(root: TreeNode, k: int) -> TreeNode:
    count = 0
    result = None

    def reverse_inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return

        # Traverse the right subtree
        reverse_inorder(node.right)

        # Process the current node
        count += 1
        if count == k:
            result = node.val
            return

        # Traverse the left subtree
        reverse_inorder(node.left)

    reverse_inorder(root)
    return result

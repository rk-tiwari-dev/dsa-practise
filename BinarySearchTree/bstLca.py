def lowestCommonAncestorInBST(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        # If both nodes are smaller than the current node, move to the left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # If both nodes are greater than the current node, move to the right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            # Current node is the LCA
            return root
    return None

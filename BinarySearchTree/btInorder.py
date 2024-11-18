def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

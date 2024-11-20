from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def constructBinaryTreeFromPostorderAndInorderTraversal(
    postorder: List[int], inorder: List[int]
) -> Optional[TreeNode]:
    if not postorder or not inorder:  # Base case: If no elements, return None
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)

    root.right = constructBinaryTreeFromPostorderAndInorderTraversal(
        postorder, inorder[root_index + 1 :]
    )

    root.left = constructBinaryTreeFromPostorderAndInorderTraversal(
        postorder, inorder[:root_index]
    )

    return root


def getInorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return getInorderTraversal(root.left) + [root.val] + getInorderTraversal(root.right)


def getPostorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return (
        getPostorderTraversal(root.left)
        + getPostorderTraversal(root.right)
        + [root.val]
    )

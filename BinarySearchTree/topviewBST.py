class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def topViewBinaryTree(root: TreeNode) -> list[int]:
    if not root:
        return []

    top_view = {}
    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)

        if hd not in top_view:
            top_view[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [top_view[hd] for hd in sorted(top_view)]

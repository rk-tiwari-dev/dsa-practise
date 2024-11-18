class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightViewBinaryTree(root: TreeNode) -> list[int]:
    result = []

    def dfs(node, depth):
        if not node:
            return

        # If this is the first time we're visiting this depth, add the node's value
        if depth == len(result):
            result.append(node.val)

        # Recur to the right and then to the left
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    # Start DFS from the root at depth 0
    dfs(root, 0)
    return result


# Example usage
def main():
    # Create a sample binary tree
    #         1
    #       /   \
    #      2     3
    #       \     \
    #        5     4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    rightNodes = rightViewBinaryTree(root)
    print("Right view of the binary tree:", rightNodes)


if __name__ == "__main__":
    main()

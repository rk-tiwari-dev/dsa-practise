def balanceBST(root: TreeNode) -> TreeNode:
    # Step 1: Perform in-order traversal to get sorted node values
    def inorderTraversal(root: TreeNode) -> list:
        if not root:
            return []
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

    # Step 2: Convert sorted array into a balanced BST
    def sortedListToBST(nums: list) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])  # The middle element becomes the root
        node.left = sortedListToBST(nums[:mid])  # Recursively build left subtree
        node.right = sortedListToBST(nums[mid + 1 :])  # Recursively build right subtree
        return node

    # Step 3: Get the sorted values of the tree using in-order traversal
    sorted_values = inorderTraversal(root)

    # Step 4: Build the balanced BST from the sorted values
    return sortedListToBST(sorted_values)

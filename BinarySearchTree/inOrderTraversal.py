# we need laern in order traversal
# in order traversal is a depth first traversal of the tree


def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.value, end=" ")
        inOrderTraversal(root.right)


# The above code is a recursive implementation of in-order traversal of a binary search tree.
# The function takes a root node as input and prints the values of the nodes in the tree in sorted order.
# The function first recursively traverses the left subtree of the root node,
# then prints the value of the root node, and finally recursively traverses the right subtree of the root node.

# The time complexity of the inOrderTraversal function is O(n), where n is the number of nodes in the binary search tree.
# This is because the function visits each node in the tree exactly once during the traversal.
# let have a look at the example we need to create a tree and then traverse it in order
# we will create a tree with the following structure


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node with the given key
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    # Search for a node with a specific key
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None or current_node.value == key:
            return current_node

        if key < current_node.value:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    # Inorder traversal (left-root-right)
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)


# Non-recursive function to find the max element in BST
def find_max_non_recursive(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    print("Maximum value in BST is:", current.value)
    return current.value


def find_min(root):
    if root is None:
        return None
    if root.left is None:
        print("Minimum value in BST is:", root.value)
        return root.value
    return find_min(root.left)


# Usage example
if __name__ == "__main__":
    bst = BinarySearchTree()
    # Insert elements into BST
    elements = [50, 30, 20, 40, 70, 60, 80]
    for element in elements:
        bst.insert(element)

    # Search for an element
    if bst.search(40):
        print("Element 40 found in the BST.")
    else:
        print("Element 40 not found in the BST.")

    # Print inorder traversal (this will print the elements in sorted order)
    print("\nInorder Traversal of the BST:")
    bst.inorder_traversal(bst.root)

    # Find the maximum element in the BST using non-recursive method
    find_max_non_recursive(bst.root)


print(inOrderTraversal(bst.root))

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        traversal = self.preorder_print(self.root, [])
        return traversal

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        if start:
            if start.value == find_val:
                return True
            return self.preorder_search(start.left, find_val)
            return self.preorder_search(start.right, find_val)
        else:
            return False

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        if start:
            traversal.append(start.value)
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)
        else:
            return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.search(4))
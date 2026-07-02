class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def createBinaryTree(self):
        # Creates the root node with key value 1
        root = Node(1)

        # Creates a left child node for the root with key value 2
        root.left = Node(2)

        # Creates a right child node for the root with key value 3
        root.right = Node(3)

        # Creates a left child node for the right child of root with key value 5
        root.right.left = Node(5)

        return root

if __name__ == "__main__":
    solution = Solution()
    root = solution.createBinaryTree()
    print(root.right.left.value)
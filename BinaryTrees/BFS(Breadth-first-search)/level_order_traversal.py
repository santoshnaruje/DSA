from collections import deque
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionUsingQueue:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = Queue()
        queue.put(root)
        result = []
        while not queue.empty():
            level = []
            queue_size = queue.qsize()
            for i in range(queue_size):
                node = queue.get(block=True)
                level.append(node.val)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            result.append(level)
        return result


class SolutionusingDeque:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])

        result = []
        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(SolutionusingDeque().levelOrder(root))
    print(SolutionUsingQueue().levelOrder(root))


if __name__ == "__main__":
    main()


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode, result) -> List[int]:
        if root is None:
            return result

        self.postorderTraversal(root.left, result)
        self.postorderTraversal(root.right, result)
        result.append(root.val)

        return result


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    S = Solution()
    result = S.postorderTraversal(root,[])
    print(result)

if __name__ == '__main__':
    main()
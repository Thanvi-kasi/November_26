# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        h = getHeight(root)
        m = h
        n = (2 ** h) - 1

        res = [[""] * n for _ in range(m)]

        def dfs(node, r, c):
            if not node:
                return

            res[r][c] = str(node.val)

            offset = 2 ** (h - r - 2)

            if node.left:
                dfs(node.left, r + 1, c - offset)

            if node.right:
                dfs(node.right, r + 1, c + offset)

        dfs(root, 0, (n - 1) // 2)

        return res

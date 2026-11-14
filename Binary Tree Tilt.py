# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def subtreeSum(node):
            if not node:
                return 0

            left_sum = subtreeSum(node.left)
            right_sum = subtreeSum(node.right)

            self.total_tilt += abs(left_sum - right_sum)

            return left_sum + right_sum + node.val

        subtreeSum(root)
        return self.total_tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        lSum = 0
        
        def helper(node: Optional[TreeNode]) -> None:

            nonlocal lSum

            if not node:
                return

            if node.left and not node.left.left and not node.left.right:
                lSum += node.left.val
                helper(node.right)
                return
            
            else:
                helper(node.left)
                helper(node.right)

        helper(root)

        return lSum
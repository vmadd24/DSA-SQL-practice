# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count = 0

        def helper(node: Optional[TreeNode]) -> None:

            nonlocal count

            if not node:
                return
            
            count += 1

            helper(node.left)
            helper(node.right)
        
        helper(root)

        return count
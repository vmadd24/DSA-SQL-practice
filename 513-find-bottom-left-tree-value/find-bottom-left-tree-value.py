# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        hmax = 0
        bottom_left = root

        def find(node: Optional[TreeNode], height: int) -> None:

            nonlocal bottom_left, hmax

            if not node:
                return

            if height > hmax:
                bottom_left = node
                hmax = height
            
            find(node.left, height+1)
            find(node.right, height+1)
        
        find(root, 0)

        return bottom_left.val
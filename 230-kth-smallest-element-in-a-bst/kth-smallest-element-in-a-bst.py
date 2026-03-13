# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        found_k = False
        kth_val = 0

        def helper(node: Optional[TreeNode]) -> None:
            
            nonlocal found_k, kth_val, k

            if node is None:
                return
            
            helper(node.left)

            k -= 1

            if k == 0:
                kth_val = node.val
                found_k = True

            if found_k:
                return

            helper(node.right)
        
        helper(root)

        return kth_val

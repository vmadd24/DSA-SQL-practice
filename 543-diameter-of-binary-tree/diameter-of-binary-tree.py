# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_global = 0

        def dfs(root: Optional[TreeNode]) -> int:

            nonlocal max_global

            if root == None:
                return 0

            left_len = dfs(root.left)
            right_len = dfs(root.right)

            max_global = max(max_global, left_len + right_len)

            return max(left_len, right_len) + 1

        dfs(root)
        return max_global
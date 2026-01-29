# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:
            p, q = q, p

        def dfs(root: 'TreeNode') -> 'TreeNode':

            if root == None or root == p or root == q:
                return root
            
            elif p.val < root.val:

                left = dfs(root.left)

                if left != None and left != p and left != q:
                    return left

                right = dfs(root.right)
            
            else:
                left = None
                right = dfs(root.right)
            
            if left == p and right == q:
                return root
            
            return left or right
        
        return dfs(root)

            
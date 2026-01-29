# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        if root == None or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p , q)

        if left != None and left != p and left != q:
            return left

        right = self.lowestCommonAncestor(root.right, p , q)

        if left and right:
            return root

        return left or right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def checkBST(root: Optional[TreeNode], min_node: Optional[TreeNode], max_node: Optional[TreeNode]):

            if root == None:
                return True
            
            if min_node and root.val <= min_node.val:
                return False
            
            if max_node and root.val >= max_node.val:
                return False
            
            return checkBST(root.left, min_node, root) and checkBST(root.right, root, max_node)
        

        return checkBST(root, None, None)

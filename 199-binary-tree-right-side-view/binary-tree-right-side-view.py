# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if root == None:
            return []
  
        rside = []
        self.right_side(root, 0, rside)
        
        return rside


    def right_side(self, node: Optional[TreeNode], level: int, rside: List[int]) -> None:
        
        if level == len(rside):
            rside.append(node.val)
        
        if node.right:
            self.right_side(node.right, level+1, rside)
        
        if node.left:
            self.right_side(node.left, level+1, rside)
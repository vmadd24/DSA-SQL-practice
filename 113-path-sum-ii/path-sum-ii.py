# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root: return []
        
        res = []
        path = [root.val]

        def dfs(node: Optional[TreeNode], s: int) -> None:

            if node and node.left == None and node.right == None:
                if s == targetSum: res.append(path.copy())
                return

            if node.left:
                path.append(node.left.val)
                dfs(node.left, s+node.left.val)
                path.pop()
            
            if node.right:
                path.append(node.right.val)
                dfs(node.right, s+node.right.val)
                path.pop()
        
        dfs(root, root.val)

        return res

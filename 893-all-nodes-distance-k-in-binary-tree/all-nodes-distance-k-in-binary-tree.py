# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        ans = []


        def find_target(node: TreeNode) -> bool:

            nonlocal k

            if node == None:
                return False

            if node == target:
                find_nodes(node, k)
                return True
            
            for child in [node.left, node.right]:
                
                if find_target(child):
                    
                    k -= 1
                    
                    if k == 0:
                        ans.append(node.val)
                    else:
                        find_nodes(node.right if child == node.left else node.left, k-1)
                    
                    return True
            
            return False
        

        def find_nodes(node: TreeNode, k: int) -> None:

            if node == None:
                return

            if k < 0:
                return
            
            if k == 0:
                ans.append(node.val)
                return
            
            find_nodes(node.left, k-1)
            find_nodes(node.right, k-1)
        

        find_target(root)
        return ans
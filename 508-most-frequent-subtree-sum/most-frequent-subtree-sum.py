# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sum_hashmap = {}

        def helper(root: Optional[TreeNode]) -> int:

            nonlocal sum_hashmap

            if not root:
                return 0
            
            combined_val = root.val + helper(root.left) + helper(root.right)
            sum_hashmap[combined_val] = sum_hashmap.get(combined_val, 0) + 1

            return combined_val
        
        helper(root)

        max_value = max(sum_hashmap.values())
        return [k for k, v in sum_hashmap.items() if v == max_value]

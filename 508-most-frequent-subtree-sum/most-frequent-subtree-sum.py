# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        sum_hashmap = {}
        max_sum = float('-inf')

        res = []

        def helper(root: Optional[TreeNode]) -> int:

            nonlocal sum_hashmap, max_sum, res

            if not root:
                return 0
            
            combined_val = root.val + helper(root.left) + helper(root.right)
            sum_hashmap[combined_val] = sum_hashmap.get(combined_val, 0) + 1

            if sum_hashmap[combined_val] == max_sum:
                res.append(combined_val)
            
            elif sum_hashmap[combined_val] > max_sum:
                max_sum = sum_hashmap[combined_val]
                res = [combined_val]

            return combined_val
        
        helper(root)

        return res
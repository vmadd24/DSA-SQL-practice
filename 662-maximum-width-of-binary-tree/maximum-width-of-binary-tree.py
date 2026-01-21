from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        my_deque = deque([(root, 1)])
        ans = 1

        while my_deque:
            
            ans = max(ans, my_deque[-1][1] - my_deque[0][1] + 1)

            for _ in range(len(my_deque)):

                elem = my_deque.popleft()
                node = elem[0]
                idx = elem[1]

                if node.left:
                    my_deque.append((node.left, 2*idx-1))
                
                if node.right:
                    my_deque.append((node.right, 2*idx))
        
        return ans
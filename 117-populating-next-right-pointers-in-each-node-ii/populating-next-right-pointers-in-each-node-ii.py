"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':


        def getNext(node: 'Optional[Node]') -> Optional[Node]:

            while(node):
                if node.left:
                    return node.left
                elif node.right:
                    return node.right
                node = node.next

            return None


        def dfs(node: 'Optional[Node]') -> None:

            if not node:
                return
            
            if node.left:
                node.left.next = node.right if node.right else getNext(node.next)
            
            if node.right:
                node.right.next = getNext(node.next)
            
            dfs(node.right)
            dfs(node.left)
        
        dfs(root)


        return root
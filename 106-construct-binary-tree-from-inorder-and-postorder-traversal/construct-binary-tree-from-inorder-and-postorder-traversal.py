# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inIndex = {x: i for i, x in enumerate(inorder)}

        def build(inStart, inEnd, postStart, postEnd) -> Optional[TreeNode]:

            if inStart > inEnd:
                return None
            
            nodeVal = postorder[postEnd]
            nodeInIndex = inIndex[nodeVal]
            leftSize = nodeInIndex - inStart

            node = TreeNode(nodeVal)
            node.left = build(inStart, nodeInIndex-1, postStart, postStart + leftSize-1)
            node.right = build(nodeInIndex+1, inEnd, postStart+leftSize, postEnd-1)

            return node
        
        return build(0, len(inorder)-1, 0, len(postorder)-1)
    



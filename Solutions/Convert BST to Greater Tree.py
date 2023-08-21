# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def convertBST(root):

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumOfValues = 0
        
        def traversal(node):
            if not node:
                return
            
            nonlocal sumOfValues
            traversal(node.right)
            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp
            traversal(node.left)
        
        traversal(root)
        return root

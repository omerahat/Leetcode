# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def invertTree(root):

    #exit condition
    if root == None:
        return None
    
    root.left , root.right = root.right , root.left

    #recursion
    invertTree(root.left)
    invertTree(root.right)

    return root


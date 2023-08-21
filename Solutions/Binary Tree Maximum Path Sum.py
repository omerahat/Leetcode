# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

answer = -float("inf") 

def maxPathSum(root):
    self.dfs(root)
    return self.answer

def dfs(self,node):
    if node is None:
        return 0
    left = self.dfs(node.left)
    right = self.dfs(node.right)

    left = max(left,0)
    right = max(right,0)

    self.answer = max(self.answer, left + right + node.val)

    return node.val + max(left,right)
    
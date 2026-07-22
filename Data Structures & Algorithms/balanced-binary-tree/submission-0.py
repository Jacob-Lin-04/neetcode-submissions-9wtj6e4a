# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
    
        def dfs_height(node):
            if node is None:
                return 0

            # Find height of left and right branch
            left = dfs_height(node.left)
            right = dfs_height(node.right)

            # Height balace must hold for every node or else whole tree is unbalanced
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        
        # Tree is balanced if dfs_height doesnt return -1
        return dfs_height(root) != -1
            




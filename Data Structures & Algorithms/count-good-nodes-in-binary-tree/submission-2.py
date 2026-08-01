# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, current_max):
            if not root:
                return 0

            new_max = max(current_max, root.val)
            # if node x is "good"
            if root.val >= current_max:
                return 1 + dfs(root.left, new_max) + dfs(root.right, new_max)
            
            return dfs(root.left, new_max) + dfs(root.right, new_max)


        return dfs(root, float('-inf'))
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

        self.good_nodes = 0

        def dfs(root, current_max):
            if not root:
                return 0

            # if node x is "good"
            if root.val >= current_max:
                self.good_nodes += 1
                
            new_max = max(current_max, root.val)

            # DFS recursivly process left and right children
            dfs(root.left,  new_max)
            dfs(root.right, new_max)
        
        dfs(root,-100)
        
        return self.good_nodes
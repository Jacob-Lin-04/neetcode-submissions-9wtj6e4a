# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        def in_order_dfs(root):
            if not root:
                return None
            
            left = in_order_dfs(root.left)
            if left is not None:
                return left

            self.counter += 1
            if self.counter == k:
                return root.val
            
            return in_order_dfs(root.right)
            
        return in_order_dfs(root)
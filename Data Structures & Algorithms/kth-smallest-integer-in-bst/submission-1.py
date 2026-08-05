# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Track how many nodes we've visited so far
        self.counter = 0
        
        def in_order_dfs(root):
            # Base case: empty subtree
            if not root:
                return None
            
            # Visit left subtree first (in-order traversal)
            # If we find the answer in left subtree, return it immediately
            left = in_order_dfs(root.left)
            if left is not None:
                return left

            # Process current node: increment counter and check if it's the kth
            self.counter += 1
            if self.counter == k:
                return root.val  # Found the kth smallest!
            
            # Visit right subtree (only if we haven't found answer yet)
            return in_order_dfs(root.right)
            
        return in_order_dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # valid node helper
        def validate(node, low, high):
            if not node:
                return True

            # Node is valid if value of left subtree is less than node value 
            #and if right subtree value is greater than node value
            if high > node.val > low:
                # Return if left and right node are valid while updating bounds for high and low
                return validate(node.left, low, node.val) and validate(node.right, node.val, high)
            else:
                return False

        
        return validate(root, -math.inf, +math.inf)
            

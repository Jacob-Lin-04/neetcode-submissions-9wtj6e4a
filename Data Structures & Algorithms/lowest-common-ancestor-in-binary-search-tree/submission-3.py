# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterative Solution
        # set current equal to root
        curr = root

        # While curr is not empty (still have nodes)
        while curr:
            # if both p and q are smaller in value than root move right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # If they are both smaller go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # Else they diverge and you found first node they seperate (LCA)
            else:
                return curr

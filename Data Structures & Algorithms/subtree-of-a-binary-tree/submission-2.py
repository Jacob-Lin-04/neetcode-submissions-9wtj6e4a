# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case
        if root == None:
            return False

        #Check if two trees are exactly the same
        def isSameTree(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False
            
            if p.val == q.val:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)

                return left and right

        # Recursvly check if subroot exists down the branch
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
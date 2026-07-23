# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfsBothTrees(p,q):
            # Base Cases
            if p == None and q == None:
                return True
            if p == None and q != None or p != None and q == None:
                return False
            
            if p.val == q.val:     
                left_same = dfsBothTrees(p.left, q.left)
                right_same = dfsBothTrees(p.right, q.right)
                return left_same and right_same
                
            else:
                return False

        return dfsBothTrees(p, q)


    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap from value -> index in inorder
        # This lets us find the root's position in O(1) time.
        inorder_map = {val: i for i, val in enumerate(inorder)}

        # Recursively reconstruct the tree using index ranges.
        # pre_start/pre_end: current segment in preorder
        # in_start/in_end: current segment in inorder
        def helper(pre_start, pre_end, in_start, in_end):
            # Base case: no nodes left to process
            if pre_start > pre_end or in_start > in_end:
                return None

            # The first value in the preorder segment is always the root
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find where the root is in the inorder segment
            # Everything to its left is the left subtree,
            # everything to its right is the right subtree.
            root_idx = inorder_map[root_val]

            # Number of nodes in the left subtree
            left_size = root_idx - in_start

            # Build left subtree:
            #  - preorder: the next left_size elements after the root
            #  - inorder: everything before root_idx
            root.left = helper(
                pre_start + 1,
                pre_start + left_size,
                in_start,
                root_idx - 1
            )

            # Build right subtree:
            #  - preorder: the remaining elements after the left subtree
            #  - inorder: everything after root_idx
            root.right = helper(
                pre_start + left_size + 1,
                pre_end,
                root_idx + 1,
                in_end
            )

            return root

        # Start with the full ranges
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
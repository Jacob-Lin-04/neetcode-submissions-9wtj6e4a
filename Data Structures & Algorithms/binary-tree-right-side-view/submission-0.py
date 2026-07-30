# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# collections dequeue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Find the last node of each level using BFS
        result = []
        

        def bfs(root):
            q = deque()

            if root:
                q.append(root)
            else:
                return []
        
            level = 0

            while len(q) > 0:
                level_size = len(q)
                for i in range(len(q)):
                    curr = q.popleft()
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    if i == level_size - 1:
                        result.append(curr.val)
                level += 1

            return result
        return bfs(root)
            


        

        
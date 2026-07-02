# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        prev = None
        curr = head

        #naive solution using hash set
        while curr:
            if curr in visited:
                return True

            visited.add(curr)

            curr = curr.next
            
        return False
        
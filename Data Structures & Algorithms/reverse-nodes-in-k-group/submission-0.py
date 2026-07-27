# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Recursive Solution
        current = head
        group = 0

        # Count up to K nodes starting at head
        while current and group < k:
            current = current.next
            group += 1

        # Once K nodes have been found
        if group == k:
            # Recursivly call the function on the node after these k nodes
            # returns head of reversed remainder
            current = self.reverseKGroup(current, k)
            
            # Reverse curren group of K nodes
            while group > 0:
                temp = head.next
                head.next = current
                current = head
                head = temp
                group -= 1

            head = current
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers technique

        slow = head
        fast = head

        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            # if there is a cycle eventually fast pointer
            # will catch up to slow pointer
            if slow == fast:
                return True

        return False




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify building the merged list
        dummy = ListNode()
        # current tracks the last node we've added to the merged list
        current = dummy

        # Loop while both lists have nodes to compare
        while list1 and list2:
            # Compare values at the front of both lists
            if list1.val < list2.val:
                # list1's node is smaller, so attach it to merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # list2's node is smaller or equal, so attach it
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            
            # Move current pointer forward to the node we just attached
            current = current.next

        # One of the lists is now empty
        # Attach all remaining nodes from whichever list still has nodes
        # (if list1 is empty, list1 evaluates to False, so list2 is used)
        current.next = list1 or list2

        # Return the actual head (skip the dummy node)
        return dummy.next
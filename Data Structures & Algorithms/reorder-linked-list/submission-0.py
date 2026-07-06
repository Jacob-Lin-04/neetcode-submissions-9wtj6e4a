# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle of the array
        # Aka the start of the secold half head

        # Reversing Linked list in place
        prev, curr = None, slow.next
        
        # terminare first half of the ListNode
        slow.next = None

        # reverese second half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # iterate through both halves
        first, second = head, prev

        while second:
            # save the next nodes
            temp1, temp2 = first.next, second.next

            # re-assign pointers to weave
            first.next = second
            second.next = temp1

            # move pointers forward
            first, second = temp1, temp2
        
        




        
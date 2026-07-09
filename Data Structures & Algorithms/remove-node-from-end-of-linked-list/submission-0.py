# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer pass
        # if first is n ahead of second second will become ListNode
        # right before the nth ListNode
        # dummy node used to allow head to have previous node
        # to handle edge case were first node is removed
        dummmy_node = ListNode(0)
        dummmy_node.next = head

        first = dummmy_node
        second = dummmy_node

        #move first across list
        for i in range(n+1):
            if first:
                first = first.next

        # second will end up on node right before nth node to remove
        while first:
            first = first.next
            second = second.next

        # remove nth node
        second.next = second.next.next

        # return head (new head if head was removed)
        return dummmy_node.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            # Iterate through each of the lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists

        return lists[0]
         
    def mergeList(self, l1, l2) ->  Optional[ListNode]:
        # Done previouslly
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists till one runs out
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            
            # Move pointer of merged list forward
            current = current.next

        # Append the remaining nodes of the non-empty list
        current.next = l1 if l1 else l2

        # The head of the merged list is right after the dummy node
        return dummy.next
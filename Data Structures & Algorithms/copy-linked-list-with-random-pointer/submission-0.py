"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use a dict (hash map) where keys are original node objects
        # and values are corresponding new node objects
        node_map = {None: None}

        curr = head
        while curr:
            # create a copy with just the values
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Connect pointer on second pass
        curr = head
        while curr:
            copy = node_map[curr]
            # map original node next/random to copy's
            # next/random
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
        
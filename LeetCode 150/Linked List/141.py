# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        if head == None:
            return False

        visited = set()

        while head.next is not None:            
            if head in visited:
                return True
            visited.update([head])
            head = head.next
            

        return False
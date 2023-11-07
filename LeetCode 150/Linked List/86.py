class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    
        smaller = ListNode(0)
        larger = ListNode(0)
        
        before = smaller
        after = larger
        
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        
        before.next = larger.next
        after.next = None
        
        return smaller.next
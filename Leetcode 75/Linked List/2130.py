# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pairs = [head.val]
        cur = head

        while cur.next:
            cur = cur.next
            pairs.append(cur.val)

        mid = len(pairs) // 2

        if len(pairs) <= 2:
            return sum(pairs)

        sums = []

        for i,j in zip(pairs[:mid], reversed(pairs[mid:])):
            sums.append(i+j)

        return max(sums)

# This solution is more in the spirit of the problem

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,linked_list):
        out = None
        while linked_list:
            out = ListNode(val=linked_list.val, next=out)
            linked_list = linked_list.next
        
        return out


    def pairSum(self, head: Optional[ListNode]) -> int:
        tot = 1

        cur = head

        # calculate total list length
        while cur.next:
            tot += 1
            cur = cur.next
        
        i = 0
        cur = head

        # divide list in two
        while i < (tot // 2):
            cur = cur.next
            i += 1
        
        secondhalf = self.rev(cur)
        ret = 0

        while secondhalf and head:
            if ret < secondhalf.val + head.val:
                ret = secondhalf.val + head.val
            secondhalf = secondhalf.next
            head = head.next

        return ret
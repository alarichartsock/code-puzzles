# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getNum(self, node):
        ret = []

        while node is not None:
            ret.append(node.val)
            node = node.next
        
        return ret


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1arr, l2arr = self.getNum(l1), self.getNum(l2)

        print(l1arr)
        print(l2arr)

        s = int(''.join(map(str,l1arr[::-1]))) + int(''.join(map(str,l2arr[::-1])))

        iterate = list(str(s))[::-1]

        head = ListNode(val=iterate[0])
        cur = head

        for num in iterate[1:]:
            cur.next = ListNode(num)
            cur = cur.next

        return head
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = ListNode(1, head)
        cur = res.next
        pre = res
        while cur is not None:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        
        return res.next



# n7 = ListNode(5, None)
# n6 = ListNode(4, n7)
# n5 = ListNode(4, n6)
# n4 = ListNode(3, n5) # cur
# n3 = ListNode(3, n4) # pre
# n2 = ListNode(2, n3)
# head = ListNode(1, n2)

n5 = ListNode(3, None)
n4 = ListNode(2, n5)
n3 = ListNode(1, n4)
n2 = ListNode(1, n3)
head = ListNode(1, n2)

s = Solution()
s.deleteDuplicates(head)
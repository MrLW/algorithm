# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(-1, head)
        cur = res.next
        pre = res
        while cur != None:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return res.next

l4 = ListNode(1, None)
l3 = ListNode(2, l4)
l2 = ListNode(3, l3)
l1 = ListNode(4, l2)
s = Solution()
s.removeElements(l1, 2)
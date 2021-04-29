# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


l1 = ListNode(1)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)
l4 = ListNode(4, l3)
l5 = ListNode(5, l4)

#    head -> 5->4->3->2->1
# 1  head -> 4->5->3->2->1
# 2  head ->
s = Solution()
print('res: ', s.reverseList(l5))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = slow = fast = ListNode(0, head)
        i = 0
        while fast != None:
            fast = fast.next
            if i > n:
                slow = slow.next
            i += 1
        slow.next = slow.next.next
        return res.next


l1 = ListNode(1)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)
l4 = ListNode(4, l3)
l5 = ListNode(5, l4)

s = Solution()
s.removeNthFromEnd(l5, 5)

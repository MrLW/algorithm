# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        题目(旋转链表): 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
        '''
        if not head: return head
        if not head.next: return head
        size = 0
        cur = head
        # 1. 计算链表总大小
        while cur:
            size += 1
            cur = cur.next
        # 2. 如果移动的步数和链表的大小相同,则相当于没有移动
        if k == size:
            return head
        if k > size:
            k = k % size
        # desc: 此时 k 肯定是小于size的
        if k == 0: return head
        # 3. 寻找头结点
        i, cur = 0, head
        res = None
        while cur:
            if size-i == k:
                res = cur
                break
            i += 1
            cur = cur.next
        # 4. 构建新的链表
        cur = res
        pre = head
        # 这里的-1其实就是减去当前cur
        remain = size - k - 1
        # 4.1 构建链表, 保证0~k个是正确的
        while k:
            if cur.next:
                k -= 1
                cur = cur.next
            else:
                cur.next = pre
        # 4.2 构建链表, 保证剩余的是正确的
        while remain:
            cur = cur.next
            remain -= 1
        cur.next = None
        return res

s = Solution()
# l1 = ListNode(2, None)
# l2 = ListNode(1, l1)
# l3 = ListNode(0, l2)
l1 = ListNode(5)
l2 = ListNode(4, l1)
l3 = ListNode(3, l2)
l4 = ListNode(2, l3)
l5 = ListNode(1, l4)
s.rotateRight(l5, 10)

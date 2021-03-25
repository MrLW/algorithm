# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        思路1: 
            1. 先用一个for循环记录每个元素出现的个数
            2. 再遍历链表, 删除出现个数大于1的元素
            该方法虽能解决问题, 但是多用了一个字典, 
        思路2: 
            其实该题的链表是有序的, 因此重复的数字只能是连续的, 利用这个特性,
            1. 遍历链表, 如果cur的值和pre的值相同, 则删除pre和cur
        '''
        res = ListNode(head.val-1, head)
        cur = res.next
        pre = res
        # pre的pre
        gpre = None
        while cur is not None:
            if pre.val != cur.val:
                gpre = pre
                pre = cur
            else:
                while cur is not None and  cur.val == pre.val:
                    cur = cur.next
                else:
                    pre = cur
                    gpre.next = pre
            if cur is not None:
                cur = cur.next
        
        return res.next

        # 思路1
        # res = ListNode(-1, head)
        # s = dict()
        # cur = head
        # while cur is not None:
        #     s[cur.val] = (s.get(cur.val) or 0) + 1
        #     cur = cur.next
        # # 重置
        # cur = res.next
        # pre = res
        # # 删除个数大于1的元素
        # while cur is not None:
        #     if s[cur.val] == 1:
        #         pre = cur
        #     else:
        #         pre.next = cur.next
        #     cur = cur.next

        return res.next


# [1,2,3,3,4,4,5]
n7 = ListNode(5, None)
n6 = ListNode(4, n7)
n5 = ListNode(4, n6)
n4 = ListNode(3, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)


# n5 = ListNode(3, None)
# n4 = ListNode(2, n5)
# n3 = ListNode(1, n4)
# n2 = ListNode(1, n3)
# head = ListNode(1, n2)

s = Solution()
s.deleteDuplicates(head)

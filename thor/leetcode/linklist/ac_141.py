# coding:utf-8

from ListNode import *
    
class Solution(object):
    """迭代法，使用快慢指针，最后两个指针遇上则存在环"""
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


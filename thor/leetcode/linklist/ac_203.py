# coding:utf-8

from ListNode import *

class Solution(object):
    """docstring for Solution"""
    def __init__(self, arg):
        super(Solution, self).__init__()
        self.arg = arg

    def removeElements(self, head:ListNode, val:int) -> ListNode:
        """
            创建一个新节点来作为整个链表的头结点，该节点中的值没有意义
            只是用来方便操作。如果用H->next=head; 
            此时操作H的话就把原先的头结点当做了一个普通节点来操作，
            原头结点就可以被删除了。最后返回H->next就满足条件了。
            正是由于有个无意义节点作为头结点会统一操作（把头结点当做普通节点）
            所以实际链表设计过程中都是有个无意义头结点的，在解决头结点问题的时候可以尝试引入
        """
        if not head:
            return None
        header = ListNode(-1)
        header.next = head
        cur = header
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return header.next


    def removeElements1(self, head:ListNode, val:int) -> ListNode:
        """
            采用复制头结点的方式进行操作，但是如果被删除的节点刚好是头结点，需要循环判断
            该方法运行超时.
        """
        if not head:
            return None

        cur = head
        pre = None
        while cur:
            if cur.val == val:
                """判断是否为头结点"""
                if cur == head:
                    head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
        return head

        
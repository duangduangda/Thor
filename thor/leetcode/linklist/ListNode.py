# coding:utf-8

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def travel(self):
        cur = self
        while cur:
            print(cur.val, end="  ")
            cur = cur.next
        print()


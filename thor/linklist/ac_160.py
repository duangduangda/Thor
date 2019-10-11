# coding:utf-8
from thor.linklist.ListNode import ListNode


class solution(object):
	"""
		快慢指针方式。让两个指针分别从两个链表头结点开始向后移动，当其中一个走到链表末尾后，
		换到另一个链表的头结点，另外一个指针也是这样，这样如果两个链表相交，根据数量关系可知，
		首次相遇的结点即为相交结点。
	"""

	def getIntersectionNode(self, headA: ListNode, headB: ListNode):
		if not headA or not headB:
			return None
		curA, curB = headA, headB
		while curA != curB:
			curA = headB if curA is None else curA.next
			curB = headA if curB is None else curB.next
		return curA

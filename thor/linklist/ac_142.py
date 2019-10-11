# coding:utf-8

class Solution(object):
	"""
		首先需要判断是否存在环，可以采用快慢指针的方式。如果存在环，fast和slow会最终相遇。
		当确认存在环，下一步就是如何判断slow在环的初始位置。再创建一个指针，当slow=entry时，
		表示为环的入口位置
	"""

	def detectCycle(self, head):
		"""
			使用三指针
		:param head: 入参链表
		:return:
		"""
		if not head or not head.next:
			return None
		slow, fast, entry = head, head, head
		while fast.next and fast:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				while slow != entry:
					slow = slow.next
					entry = entry.next
				return entry
		return None

	def detectCycle1(self, head):
		"""
			使用双指针
		:param head:入参链表
		:return:
		"""
		if not head or not head.next:
			return None
		slow, fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if fast == slow:
				"""确认存在环"""
				fast = head
				while slow != fast:
					slow = slow.next
					fast = fast.next
				return fast
		return None

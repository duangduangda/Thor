# coding:utf-8

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def travel(self):
		cur = self
		while cur.next:
			print(cur.val, end = "  ")
			cur = cur.next
		print(cur.val)

	def append(self, val):
		node = ListNode(val)
		cur = self
		while cur.next:
			cur = cur.next
		cur.next = node
		return self

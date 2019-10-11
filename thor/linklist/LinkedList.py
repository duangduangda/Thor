# coding:utf-8
from thor.linklist.ListNode import ListNode


class LinkedList(object):
	def __init__(self):
		self.head = None

	def add_at_head(self, val):
		node = ListNode(val)
		node.next = self.head
		self.head = node

	def add_at_tail(self, val):
		node = ListNode(val)
		if not self.head:
			self.head = node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = node

	def to_string(self):
		cur = self.head
		while cur:
			print(cur.val, end = "    ")
			cur = cur.next
		print()

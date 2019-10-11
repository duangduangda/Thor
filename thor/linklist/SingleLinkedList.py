# coding:utf-8

class SingleLinkedList(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.head = None

	def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if index < 0 or index >= self.length():
			return -1
		else:
			count = 0
			cur = self.head
			while count < index:
				count += 1
				cur = cur.next
			return cur.element

	def addAtHead(self, val: int) -> None:
		"""
		Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
		"""
		node = Node(val)
		node.next = self.head
		self.head = node

	def addAtTail(self, val: int) -> None:
		"""
		Append a node of value val to the last element of the linked list.
		"""
		node = Node(val)
		if self.head is None:
			self.head = node
		else:
			cur = self.head
			while cur.next is not None:
				cur = cur.next
			cur.next = node

	def addAtIndex(self, index: int, val: int) -> None:
		"""
		Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
		"""
		pre = self.head
		count = 0
		if index <= 0:
			self.addAtHead(val)
		elif index > self.length():
			pass
		elif index == self.length():
			self.addAtTail(val)
		else:
			while count < (index - 1):
				count += 1
				pre = pre.next
			node = Node(val)
			node.next = pre.next
			pre.next = node

	def deleteAtIndex(self, index: int) -> None:
		"""
		Delete the index-th node in the linked list, if the index is valid.
		"""
		count = 0
		cur = self.head

		if index < 0 or index >= self.length():
			print("invalid index")
			return
		elif index == 0:
			self.head = cur.next
			return
		else:
			pre = None
			while count < index:
				count += 1
				pre = cur
				cur = cur.next
			pre.next = cur.next

	def length(self) -> int:
		"""
			the length of list
		"""
		cur = self.head
		count = 0
		while cur is not None:
			count += 1
			cur = cur.next
		return count


class Node(object):
	def __init__(self, element):
		self.element = element
		self.next = None

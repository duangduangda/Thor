# coding:utf-8


class DoubleLinkedList(object):

	def __init__(self):
		self.head = None

	def get(self, index) -> int:
		if index < 0 or index >= self.length():
			print("Invalid index %d." % index)
			return -1
		else:
			count = 0
			cur = self.head
			while count < index:
				count += 1
				cur = cur.next
			return cur.element

	def add_at_head(self, val):
		node = Node(val)
		if self.head is None:
			self.head = node

		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

	def add_at_tail(self, val):
		node = Node(val)
		if self.head is None:
			self.head = node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def add_at_index(self, index, val):
		if index > self.length():
			print("Invalid index %d" % index)
			return None
		elif index <= 0:
			self.add_at_head(val)
		elif index == self.length():
			self.add_at_tail(val)
		else:
			count = 0
			cur = self.head
			while count < (index - 1):
				count += 1
				cur = cur.next
			node = Node(val)
			node.next = cur.next
			node.prev = cur
			cur.next.prev = node
			cur.next = node

	def delete_at_index(self, index):
		if index < 0 or index >= self.length():
			print("Invalid index %d,will not delete any element" % index)
			return None
		elif index == 0:
			cur = self.head
			self.head = cur.next
			if cur.next is not None:
				cur.next.prev = cur.prev
		elif index == self.length() - 1:
			cur = self.head
			while cur.next:
				cur = cur.next

			cur.prev.next = cur.next

		else:
			cur = self.head
			count = 0
			while count < index:
				count += 1
				cur = cur.next
			cur.prev.next = cur.next
			cur.next.prev = cur.prev

	def travel(self):
		cur = self.head
		while cur is not None:
			print(cur.element, end="\t")
			cur = cur.next
		print()

	def length(self):
		cur = self.head
		count = 0
		while cur is not None:
			cur = cur.next
			count += 1
		return count


class Node(object):
	def __init__(self, val):
		self.element = val
		self.prev = None
		self.next = None


def main():
	dll = DoubleLinkedList()
	# print(dll.add_at_head(1))
	# print(dll.add_at_tail(3))
	# print(dll.add_at_index(1, 2))
	# print(dll.get(1))
	# dll.travel()
	# print(dll.delete_at_index(1))
	# print(dll.get(1))

	# dll.add_at_head(5)
	# dll.add_at_head(2)
	# dll.delete_at_index(1)
	# dll.add_at_index(1, 9)
	# dll.add_at_head(4)
	# dll.add_at_head(9)
	# dll.add_at_head(8)
	# dll.get(3)
	# dll.add_at_tail(1)
	# dll.add_at_index(3, 6)
	# dll.add_at_head(3)

	dll.add_at_head(1)
	dll.delete_at_index(0)


if __name__ == '__main__':
	main()

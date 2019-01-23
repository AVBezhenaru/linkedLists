
class Node:
	def __init__(self, v):
		self.value = v
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

	def print_all_nodes(self):
		node = self.head

		while node is not None:
			print(node.value)
			node = node.next	

	def find(self, val):
		node = self.head

		if node is None:
			return print("linkedList is empty")

		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None

	def find_all(self, val):
		node = self.head
		f_list = []

		if node is None:
			return print("linkedList is empty")

		while node is not None:
			if node.value == val:
				f_list.append(val)
			node = node.next
		return f_list

	def delete(self, val, all):
		node = self.head
		prev = None

		if node is None:
			return print("linkedList is empty")

		while node.next is not None:
			if node.value == val and prev is None:
				node = node.next
				self.head = node

				if all == False:
					return
				continue

			if node.value == val:

				if all == True:

					while node.value == node.next.value:
						node = node.next

				prev.next = node.next

				if all == False:
					return

			prev = node
			node = node.next

		if node.next is None and prev is None and val == node.value:
			self.head = None

		elif node.next is None and node.value == val:
			prev.next = None

	def clean(self):
		self.head = None

	def len(self):
		node = self.head
		count = 0

		if node is None:
			return print("linkedList is empty")

		while node is not None:
			count = count + 1
			node = node.next
		return count

	def insert(self, afterNode, newNode):
		if self.head is None:
			self.add_in_tail(Node(newNode))
			return

		node = self.head
		after = None
		nNode = None

		while node is not None:
			if node.value == afterNode:
				after = node.next
				nNode = Node(newNode)
				node.next = nNode
				nNode.next = after
				return

			node = node.next

# sumLinkListFunction

def sumLinkList(list1, list2):
	if list1.len() != list2.len():
		return print("linked lists are not the same")

	buf = list1.head
	buf2 = list2.head
	sumBuf = None
	list3 = LinkedList()
	while buf is not None:
		sumBuf = buf.value + buf2.value
		buf = buf.next
		buf2 = buf2.next
		list3.add_in_tail(Node(sumBuf))
	return list3.print_all_nodes()



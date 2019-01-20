
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
		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None

	def find_all(self, val):
		node = self.head
		count = 0
		f_list = []
		while node is not None:
			if node.value == val:
				f_list.append(val)
				count = count + 1
			node = node.next
		return f_list

	def delete(self, val, all):
		node = self.head
		prev = None

		while node.next is not None:
			if node.value == val and prev is None:
				node = node.next
				self.head = node

				if all == False:
					return
				continue

			elif node.value == val:

				if all == True:

					while node.value == node.next.value:
						node = node.next

				prev.next = node.next

				if all == False:
					return

			prev = node
			node = node.next

		if node.next == None:
			prev.next = None

	def clean(self):
		node = self.head
		while node is not None:
			node.value = None
			node = node.next

		return None

	def len(self):
		node = self.head
		count = 0
		while node is not None:
			count = count + 1
			node = node.next
		return count

	def insert(self, afterNode, newNode):
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



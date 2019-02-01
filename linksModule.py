
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
			return None

		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None

	def find_all(self, val):
		node = self.head
		f_list = []

		if node is None:
			return f_list

		while node is not None:
			if node.value == val:
				f_list.append(node)
			node = node.next
		return f_list

	def delete(self, val, all=False):
		currentNode = self.head
		prevNode = None

		if currentNode is None:
			return

		if currentNode.next is None:
			self.head = None
			self.tail = self.head

		while currentNode is not None:
			if currentNode.value == val:
				self.head = currentNode.next
				if currentNode.next is None:
					self.tail = self.head
				currentNode = currentNode.next

				if all == True:
					continue
				else:
					return

			elif currentNode.next is None:
				currentNode.next = None
				return

			elif currentNode.next.value == val:

				if all == False:
					currentNode.next = currentNode.next.next
					self.tail = currentNode
					return

				prevNode = currentNode

				while currentNode.next.value == val:
					currentNode = currentNode.next

					if currentNode.next is None:
						prevNode.next = None
						self.tail = prevNode
						return

					prevNode.next = currentNode.next

			currentNode = currentNode.next

	def clean(self):
		self.head = None

	def len(self):
		node = self.head
		count = 0

		if node is None:
			return count

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
	return list3



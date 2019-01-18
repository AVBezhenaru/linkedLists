
class Node:
	def __init__(self, v):
		self.value = v
		self.next = None

n1 = Node(12)
n2 = Node(55)

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


s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(Node(12))
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(11))
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(11))
s_list.print_all_nodes()
print("after delete Nodes")
s_list.delete(11, all=False)
s_list.insert(12, 33)
s_list.print_all_nodes()

print()
print("Find")

nf = s_list.find(128)
if nf is not None:
	print(nf.value)

print("Find all")

nf1 = s_list.find_all(128)
if nf1 is not None:
	print(nf1)

print()

s_list.clean()
s_list.print_all_nodes()

nf = s_list.find(55)
if nf is not None:
	print(nf.value)

print("LinkedList length:", s_list.len())


n3 = Node(3)
n4 = Node(4)

n3.next = n4

print("n3", n3.next)
print("n4", n4.next)

# def sumLinkList(list1, list2):
# 	list3 = None
# 	if list1.len() == list2.len():
# 		for i in list1.len():
# 			print list1(i)
# 			# list3.add_in_tail(Node(list1(i) + list2(i)))
# 	return List1
#
# s_list3 = LinkedList()
# s_list3.add_in_tail(Node(12))
# s_list4 = LinkedList()
# s_list4.add_in_tail(Node(12))
# print("sumList", sumLinkList(s_list3, s_list4))

from linksModule import *

n1 = Node(12)
n2 = Node(55)

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

# s_list.clean()
# s_list.print_all_nodes()

nf = s_list.find(55)
if nf is not None:
	print(nf.value)

print("LinkedList length:", s_list.len())


n3 = Node(3)
n4 = Node(4)

n3.next = n4

print("n3", n3.next)
print("n4", n4.next)

def sumLinkList(list1, list2):
	buf = list1.head
	buf2 = list2.head
	sumBuf = None
	list3 = LinkedList()
	while buf.next is not None:
		sumBuf = buf.value + buf2.value
		buf = buf.next
		buf2 = buf2.next
		list3.add_in_tail(Node(sumBuf))
	return list3.print_all_nodes()

sumLinkList(s_list, s_list)


from linksModule import *
from test import *

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
print("clean list")
s_list.print_all_nodes()

nf = s_list.find(55)
if nf is not None:
	print(nf.value)

print("LinkedList length:", s_list.len())

sumLinkList(s_list, s_list)


deleteTest(s_list, 128, True)
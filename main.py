from linksModule import *
from random import *
from test import *

# def autoCompleteList(countNodes, valueRange):
# 	list = LinkedList()
# 	for i in range(countNodes):
# 		list.add_in_tail(Node(randint(0, valueRange)))
# 	return list
#
# list = autoCompleteList(5, 100)

firstList = LinkedList()
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
# firstList.add_in_tail(Node(1))
# firstList.add_in_tail(Node(3))
# firstList.add_in_tail(Node(2))
# firstList.add_in_tail(Node(1))

deleteTest(firstList, 1, False)

#
# # firstList.delete(1, False)


# print("before delete nodes")
# firstList.print_all_nodes()
# firstList.delete(1, True)
# print("after delete nodes")
# firstList.print_all_nodes()
#
#
# print()
# print("Find")
#
# nf = s_list.find(128)
# if nf is not None:
# 	print(nf.value)
#
# print("Find all")
#
# nf1 = s_list.find_all(128)
# if nf1 is not None:
# 	print(nf1)
#
# print()
#
# # s_list.clean()
# print("clean list")
# s_list.print_all_nodes()
#
# nf = s_list.find(55)
# if nf is not None:
# 	print(nf.value)
#
# print("LinkedList length:", s_list.len())
#
# sumLinkList(s_list, s_list)
#
#
# deleteTest(s_list, 128, True)
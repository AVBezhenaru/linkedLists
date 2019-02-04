from linksModule import *
from random import *
from test import *

firstList = LinkedList()
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
# firstList.add_in_tail(Node(2))
# firstList.add_in_tail(Node(2))
# firstList.add_in_tail(Node(2))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))



def deleteTest1(list):
	list.delete(2, True)
	b = list.len()

	if b == 6 and list.head.value == 1 and list.tail.value == 3:
		print("Test OK")
	else:
		print("Test ERROR")

def deleteTest2(list):
	list.delete(1, True)
	b = list.len()

	if b == 6 and list.head.value == 2 and list.tail.value == 3:
		print("Test OK")
	else:
		print("Test ERROR")

def deleteTest3(list):
	list.delete(3, True)
	b = list.len()

	if b == 6 and list.head.value == 1 and list.tail.value == 2:
		print("Test OK")
	else:
		print("Test ERROR")

def deleteTest4(list):
	list.delete(1, True)
	b = list.len()

	if b == 3 and list.head.value == 2 and list.tail.value == 2:
		print("Test OK")
	else:
		print("Test ERROR")

def deleteTest5(list):
	list.delete(1, True)
	b = list.len()

	if b == 0 and list.head == None and list.tail == None:
		print("Test OK")
	else:
		print("Test ERROR")


# print("Delete test1")
# deleteTest1(firstList)
# print()
# print("Delete test2")
# deleteTest2(firstList)
# print()
print("Delete test4")
deleteTest5(firstList)
print()
# print("Insert test")
# insertTest(firstList, 3, 5)
# print()
# print("Length test test")
# lengthTest(firstList)
# print()
# print("Find all test")
# findAllTest(firstList, 1)
# print()
# print("sum list function")
# sumLinkList(firstList, firstList)
# print()
# print("Clean test")
# cleanTest(firstList)


# print("lenght", firstList.len())
# print("head",firstList.head)
# print("tail",firstList.tail)
# print("head",firstList.head.value)
# print("tail",firstList.tail.value)
# print("before")
# firstList.print_all_nodes()
# b = firstList
# print("bbbbbb", b)
# firstList.delete(2)
# a = firstList
# print("after aaaaaaaaaa", a)
# firstList.print_all_nodes()
# print("Node after delete function")
# print("head",firstList.head)
# print("tail",firstList.tail)
# print("head",firstList.head.value)
# print("tail",firstList.tail.value)
# print("lenght", firstList.len())


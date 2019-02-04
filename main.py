from linksModule import *
from random import *
from test import *

firstList = LinkedList()
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))

secondList = LinkedList()
secondList.add_in_tail(Node(1))
secondList.add_in_tail(Node(1))
secondList.add_in_tail(Node(1))
secondList.add_in_tail(Node(4))



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


# firstList.insert(2, 3)
# firstList.print_all_nodes()
# print("head", firstList.head.value)
# print("tail", firstList.tail.value)

b = sumLinkList(firstList, secondList);
print(b.tail.value)

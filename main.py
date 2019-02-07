from linksModule import *
from random import *
from test import *

# firstList = LinkedList()
# firstList.add_in_tail(Node(1))
# firstList.add_in_tail(Node(3))
# firstList.add_in_tail(Node(1))
# firstList.add_in_tail(Node(1))
# secondList = LinkedList()
# secondList.add_in_tail(Node(1))
# secondList.add_in_tail(Node(1))
# secondList.add_in_tail(Node(1))
# secondList.add_in_tail(Node(4))


def insertTest1():
	print('Insert Test 1')
	list = LinkedList()
	list.insert(list.find(1), Node(1))
	a = list.len()
	if list.head.value == 1 and list.tail.value == 1 and a == 1:
		print("Test OK")
	else:
		print("Test ERROR")

def insertTest2():
	print('Insert Test 2')
	list = LinkedList()
	list.add_in_tail(Node(1))
	list.insert(list.find(1), Node(3))
	a = list.len()
	if list.head.value == 1 and list.tail.value == 3 and a == 2:
		print("Test OK")
	else:
		print("Test ERROR")

def insertTest3():
	print('Insert Test 3')
	list = LinkedList()
	list.add_in_tail(Node(1))
	list.add_in_tail(Node(3))
	list.insert(list.find(1), Node(2))
	a = list.len()
	if list.head.value == 1 and list.tail.value == 3 and a == 3:
		print("Test OK")
	else:
		print("Test ERROR")

insertTest1()
insertTest2()
insertTest3()


# def deleteTest1(list):
# 	list.delete(2, True)
# 	b = list.len()
#
# 	if b == 6 and list.head.value == 1 and list.tail.value == 3:
# 		print("Test OK")
# 	else:
# 		print("Test ERROR")
#
# def deleteTest2(list):
# 	list.delete(1, True)
# 	b = list.len()
#
# 	if b == 6 and list.head.value == 2 and list.tail.value == 3:
# 		print("Test OK")
# 	else:
# 		print("Test ERROR")
#
# def deleteTest3(list):
# 	list.delete(3, True)
# 	b = list.len()
#
# 	if b == 6 and list.head.value == 1 and list.tail.value == 2:
# 		print("Test OK")
# 	else:
# 		print("Test ERROR")
#
# def deleteTest4(list):
# 	list.delete(1, True)
# 	b = list.len()
#
# 	if b == 3 and list.head.value == 2 and list.tail.value == 2:
# 		print("Test OK")
# 	else:
# 		print("Test ERROR")
#
# def deleteTest5(list):
# 	list.delete(1, True)
# 	b = list.len()
#
# 	if b == 0 and list.head == None and list.tail == None:
# 		print("Test OK")
# 	else:
# 		print("Test ERROR")




# b = sumLinkList(firstList, secondList);
# print(b.tail.value)

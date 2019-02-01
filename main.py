from linksModule import *
from random import *
from test import *

firstList = LinkedList()
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(2))
firstList.add_in_tail(Node(2))
firstList.add_in_tail(Node(2))
firstList.add_in_tail(Node(3))
firstList.add_in_tail(Node(3))
# firstList.add_in_tail(Node(2))
# firstList.add_in_tail(Node(1))



print("Delete test")
deleteTest(firstList, 2, True)
print()
print("Insert test")
insertTest(firstList, 3, 5)
print()
print("Length test test")
lengthTest(firstList)
print()
print("Find all test")
findAllTest(firstList, 1)
print()
print("sum list function")
sumLinkList(firstList, firstList)
print()
print("Clean test")
cleanTest(firstList)


# print("lenght", firstList.len())
# print("head",firstList.head)
# print("tail",firstList.tail)
# print("head",firstList.head.value)
# print("tail",firstList.tail.value)
# print("before")
# firstList.print_all_nodes()
# firstList.delete(2, True)
# print("after")
# firstList.print_all_nodes()
# print("Node after delete function")
# print("head",firstList.head)
# print("tail",firstList.tail)
# print("head",firstList.head.value)
# print("tail",firstList.tail.value)
# print("lenght", firstList.len())


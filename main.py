from linksModule import *
from random import *
from test import *

firstList = LinkedList()
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(1))
firstList.add_in_tail(Node(3))
firstList.add_in_tail(Node(2))
firstList.add_in_tail(Node(1))

print("Delete test")
deleteTest(firstList, 1, False)
print()
print("Insert test")
insertTest(firstList, 3, 5)
print()
print("Length test test")
lengthTest(firstList)
print()
print("Find all test")
findAllTest(firstList, 2)
print()
print("sum list function")
sumLinkList(firstList, firstList)
print()
print("Clean test")
cleanTest(firstList)

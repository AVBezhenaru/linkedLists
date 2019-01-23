from linksModule import *
# tests

def deleteTest(list, val, all):
    if list.head == None:
        print("Linked list is empty")
        return

    print("before delete")
    list.print_all_nodes()
    a = list.find_all(val)
    if a == []:
        print(val, "There is no such value in this list")

    if all == True:
        list.delete(val, all)
        b = list.find_all(val)
        if b == [] or b is None:
            print("Delete test OK \nAfter delete")
            list.print_all_nodes()
        else:
            print("Delete test FAIl")

    elif all == False:
        a = list.find_all(val)
        list.delete(val, all)
        b = list.find_all(val)
        if b is None or a > b:
            print("Delete test OK \nAfter delete")
            list.print_all_nodes()
        else:
            print("Delete test FAIl")

def cleanTest(list):
    if list.head == None:
        print("Linked list is empty")
        return

    print("before clean")
    list.print_all_nodes()

    a = list.clean()
    if a == None:
        print("Clean test OK \nAfter clean")
        list.print_all_nodes()
    else:
        print("Clean test OK \nAfter clean")
        list.print_all_nodes()

def findAllTest(list, val):
    if list.head == None:
        print("Linked list is empty")
        return

    print("Linked list")
    list.print_all_nodes()

    a = list.find_all(val)
    if a == []:
        print(val, "Find test FAIL \nThere is no such value in this list")

    else:
        print("Find test OK \nFind all", a)

def lengthTest(list):
    if list.head == None:
        print("Linked list is empty")
        return

    print("Linked list")
    list.print_all_nodes()

    a = list.len()
    print("length is", a)
    list.add_in_tail(Node(1))
    b = list.len()
    if a < b:
        print("length after add one node is", b, "\nFind test OK")

    else:
        print("Find test FAIL")

def insertTest(list, afterNode, newNode):
    list.print_all_nodes()
    a = list.len()
    print("length is", a)
    list.insert(afterNode, newNode)
    b = list.len()
    if a is None or a < b:
        print("Linked list")
        list.print_all_nodes()
        print("length after insert node is", b, "\nFind test OK")

    else:
        print("Find test FAIL")
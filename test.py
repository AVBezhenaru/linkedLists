# tests
#
# def cleanTest(list):
# 	a = list.clean()
# 	if a == None:
# 		print("cleanTest ok", a)
# 	else:
# 		print("cleanTest fail", a)

def deleteTest(list, val, all):
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

# def findAllTest(list, val):
# 	a = list.find_all(val)
# 	if a == []:
# 		print("number not found")
# 		return
#
# 	for i in a:
# 		print("print a index", a.[i])
# 		if val != a.index(i):
# 			print("findAllTest fail")
# 			return
# 		else:
# 			print("findAllTest ok")


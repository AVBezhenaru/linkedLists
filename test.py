# tests

def cleanTest(list):
	a = list.clean()
	if a == None:
		print("cleanTest ok", a)
	else:
		print("cleanTest fail", a)

def deleteTest(list, val, all):
	a = list.len()
	list.delete(val, all)
	b = list.len()
	if a > b:
		print("deleteTest ok", a)
	else:
		print("deleteTest fail", a)

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


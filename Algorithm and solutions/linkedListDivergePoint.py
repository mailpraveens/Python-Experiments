def findDivergePointForOfTwoLinkedLists(list1, list2):
	# Assuming the list class has a method length to give the length of the list
	lengthList1 = list1.length()
	lengthList2 = list2.length()
	differnce = lengthList2 - lengthList1
	if(lengthList2>=lengthList1):
		while(differnce!=0):
			list2 = list2.next
			differnce -= 1

	else:
		while (differnce!=0):
			list1 = list1.next
			differnce += 1 #Notice the addition, that is because the difference will be negative 


	while(list1 and list2 and list1 != list2):
		list1 = list1.next
		list2 = list2.next

	if(list1 != None and list2 == None):
		return None
	if(list1 == None and list2 != None):
		return None
	return list1

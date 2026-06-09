# Extend Method

list1=["Orange","Mango","Ali",10,True, [10,"Ibtisam",False]]
print("List 1: ",list1)

list2 = [1, 3, 5, True,{"Ali": 20, "Ibtisam": 30}]
print('List 2:', list2)

list1.extend(list2)
print('Extended List 1:', list1)

list2.append(list1)
print('Appended List 2:', list2)




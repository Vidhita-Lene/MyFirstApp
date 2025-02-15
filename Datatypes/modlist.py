#list is a mutable datatype: values or objects can be changed
#list modification : with help of index
empName = ["shruti","piya","janvi","shreya"]
print(empName)
empName[1]="priya"
print(empName)
empName[-2] = "janhavi"
print(empName)

#to delete a list item
del empName[0]
print("list after deletion:" ,empName)
empName[1] = "tiya"
print("modify after deletion= ",empName)

empName = ["shruti","piya","janvi","shreya"]
empName[4]="jiya"    #cannot modify list if it is out of range
print(empName)
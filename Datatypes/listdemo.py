course=["python","java","aws"]
marks=[2.4,3.4,4.5]
numbers=[1,2,3,4]
mixed=[1,4.4,True,"python",3j]

print(course)
print(marks)
print(numbers)
print(mixed)

#duplicates
duplilist=[2,2,33,33,5,6,7]
print("course list=",course)
print("type=",type(course))
print("length of list=",len(course))

#accesing each element of list using index(starts from 0)
print("element at index 0=", course[0])
print("element at index 1=", course[1])
print("element at index 2=", course[2])
print ("last element = ", course[-1])

#slicing - accesing a sub list slice[start:end] : (end is excluded)
marks=[23,55,67,88,89,100]
print("marks listy =", marks)
print("accessing using slicing = ",marks[2:6])
print("negative slicing= ",marks[1:-1])
print("whole slicing=" ,marks[:5])
print("whole negative slicing=", marks[-6:-1])
print()

#concatination : joining two list.(using + opearator)
numList1=[1,2,3,4,5]
numList2=[5,6,7,8,9,10]
concate=numList1+numList2
print(concate)

concate1=numList1+[55,66,77]
print(concate1)
print("concate using , = ",numList1,numList2)
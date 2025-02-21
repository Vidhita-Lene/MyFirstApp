#1. Write a Python program that:

#Creates an empty list.
#Appends the numbers 10, 20, and 30 to the list one by one.
#Prints the final list.

my_list=[]
my_list.append(10)
print(my_list)
my_list.append(20)
print(my_list)
my_list.append(30)
print(my_list)
print('-'*50)
#2. Use extend() to Merge Lists
#Takes two lists as input.
#Extends the first list with the second list using extend().
#Prints the updated first list.
#Example Input:
list1 = [1, 2, 3]  
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
print('-'*50)
#3. Takes a list, an element, and an index as input.
#Inserts the element at the given index using insert().
#Prints the updated list.

#Example Input:

#list1 = [10, 20, 30, 50]  
#element = 40  
#index = 3
list1=[10, 20, 30, 50]
list1.insert(3,40)
print(list1)
print('-'*50)
#4. Append a List Inside Another List

#Takes two lists as input.
#Appends the second list as a single element inside the first list.
#Prints the updated list.
#Example Input:
#list1 = [1, 2, 3]  
#list2 = [4, 5, 6]

list1=[1,2,3]

list1.append(list2)
print(list1)
#list=list1.append(5)
#print(list)
print('-'*50)
#5. Use All Three Methods in One Program
#Write a Python program that:

#Starts with a list [1, 2, 3].
#Appends 4 to the list.
#Extends the list with [5, 6].
#Inserts 0 at the beginning.
#Prints the final list.
#Expected Output:
#[0, 1, 2, 3, 4, 5, 6]

list=[1,2,3]
list.append(4)
print(list)
list.insert(0,0)
print(list)
list.append(5)
print(list)
list.append(6)
print(list)

# num1=int(input("enter a number"))
# num2=int(input("enter a number"))
# add=num1+num2
# sub=num1-num2
# mul=num1*num2
# div=num1/num2
# modulus=num1%num2
# expo=num1**num2
# floordiv=num1//num2
# print("add is",add)
# print("sub is",sub)
# print("mul is",mul)
# print("div is",div)
# print("mod is",modulus)
# print("exponet is",expo)
# print("floor division is",floordiv)
#logical
# x=56
# y=67
# print(x>y and x!=y)
# print(x>y or x!=y)
# print(not(x>y))
#membership operator: checks if given value is present or not (in,not in)
# list1=23,45,67,34
# num=int(input("enetre a number"))
# if(num in list1):
#     print(f"{num} is present in list")
# else:
#     print(f"{num} is not in list")

#identity operator
list1=[1,2,3]
list2=[1,2,3]
list3=list1
print(list1 is list2)
print(id(list1), id(list2))
print(list3 is list1)
print(id(list3),id(list1))
print(list3 is not list1)
print(id(list3),id(list1))

#assignment oparator
a=7
b=6
#a=a+b
a+=b
print(a)
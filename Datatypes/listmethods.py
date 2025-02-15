#methods in list.
#1. append: t will only add single element at end of list
fruits=["apple","banana","chikko","pineapple"]
fruits.append("berry")
print(fruits)

#2.extend: it will add another list to original list at end
fruits=["apple","banana","chikko","pineapple"]
fruits.extend(["cherry","mango"])
print(fruits)
fruits.extend("mango")  # adds in list as a iterable character
print(fruits)
fruits.extend(("cherry","mango"))  #tuple also gets added
print(fruits)
print()

#3.insert : it will add an element at particular position
fruits=["apple","banana","chikko","pineapple"]
fruits.insert(1,"mango")
print(fruits)
#clear - removes all the element from the list
fruits=["mango","grapes","cherry"]
print(fruits)
print('-'*50)
fruits.clear()
print(fruits)
print('-'*50)

fruits.extend(["mango","banana","orange"])
print(fruits)
print('-'*50)

fruits.remove('banana')
print("using remove method:", fruits)
print('-'*50)

fruits.pop(1)
print("using pop method", fruits)

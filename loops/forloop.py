#range()- it gives iterates the sequence
#range(start,stop,step)

x=range(1,11)  # last element is excluded
print(list(x))

a=range(7)
print(list(a))

b=range(1,11,2)
print(list(b))

marks=[88,99,100,56,78,19,91]
#print(marks[0])
#print(marks[1])
#print(marks[2])
for i in marks:
    print(i)

for num in range(1,10,2):
    print(num)

#break-  it is used to terminate a block of code or that iteration
# num=[1,2,3,4,5,6,7]
# for element in num:
#     if(element==5):
#         break
#     print(element)

#continue- it skips that particular iteration and executes rest of the iteration.
# num=[1,2,3,4,5,6,7]
# for i in num:
#     if(i==3 or i==5):
#         continue
#     print(i)

# string="january"
# for letter in string:
#     if(letter=="n" or letter=="r"):
#         break
#     print(letter)
    
# string="january"
# for letter in string:
#     if(letter=="n" or letter=="r"):
#         continue
#     print(letter)

#using while loop
string="january"
count=0
while(count<len(string)):
    if("u" in string[count]):
        break
    print(string[count])
    count=count+1   
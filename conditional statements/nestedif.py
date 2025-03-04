age=int(input("enter a number"))
citizen=input("are you citizen of india(yes/no)").lower()

if(age>=18):
    if(citizen=="yes"):
        print("you are eligible to vote")
    else:
        print("you  must be citizen of india")
else:
    print("you are not eligible to vote")
    
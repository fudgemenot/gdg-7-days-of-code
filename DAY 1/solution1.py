ans="y"
while ans=="y" or ans=="Y":
    a=input("enter a word:")
    if a.isalpha()==True:
        print(a,a)
    else:
        print("This function do not support alphanumeric/numeric inputs")
    ans= input("To enter more word press y or Y,to exit press any other key:")




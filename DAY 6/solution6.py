ans="y"

while ans.lower()=="y":
    str=input("enter a sentence:").split()
    l=["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    count=0
    for i in str:
        for j in i:
            if j in l:
                count=count+1
    print(count)
    ans=input("Press 'Y' or 'y' to continue, otherwise press any key to exit:" )




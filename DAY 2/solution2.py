ans="y"
while ans.lower()=="y":
    N=int(input("Enter the number of lines you want in the pyramid:"))
    for i in range(1,N+1):
        for j in range(1,(N+1)-i):
          print(" ",end="")
        for k in range(1,2*i):
          print("*",end="")
        print()    
    ans=input("Press 'Y' or 'y' to continue, otherwise press any key to exit:" )

#time:around 7-8 minutes(including every process)#

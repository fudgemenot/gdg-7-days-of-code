ans="y"
while ans.lower()=="y":
    while True:
       n=int(input("enter the no.of input you want in array(n):"))
       arr=input("enter the value you want to put in array:").split()
      
       if not len(arr)==n:
           print("Error: You have entered more than {n} elements.")
           continue
       break
    a= [int(x) for x in arr]
    sum=0
    for i in a:
        if i>0:
          sum=sum+i


    print(sum)
    ans=input("Press 'Y' or 'y' to continue, otherwise press any key to exit:" )


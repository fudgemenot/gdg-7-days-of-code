ans="y"
print("Enter two digit to give the range.Make sure that both the inputs are not negative and satisfies the condition a<b")
while ans.lower()=="y":
    while True:
       a = input("Enter the first non-negative integer: ")
       b = input("Enter the second non-negative integer: ")
      
       if not a.isdigit() or not b.isdigit():
           print("Make sure that inputs are non-negative integrers. Please try again.")
           continue
       c = int(a)
       d = int(b)
       if c< 0 or d< 0:
         print("Both the inputs should be non-negative integers. Please try again.")
         continue     
       if c>= d:
          print("The input is not satisfying the condition a < b. Please try again.")
          continue
       break 
    for i in range(c,d+1):
         if i%5==0 and i%7==0:
            print("Foobar")
         elif i%5==0:
            print("Foo")
         elif i%7==0:
            print("bar")
         else:
            print("baz")
    
    ans=input("Press 'Y' or 'y' to continue, otherwise press any key to exit:" )
    
#time: around 10-15 mins(including debugging)#

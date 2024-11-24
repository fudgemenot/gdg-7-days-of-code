print("Please enter the matrix dimensions.")
print("You will need to input two integers: the number of rows and the number of columns.")
print("Example: For a 3x3 matrix, you would enter '3' for rows and '3' for columns.\n")

ans="y"
while ans.lower()=="y":
    n=int(input("Enter number of rows (positive integer): "))
    m=int(input("Enter number of columns (positive integer): "))
    mat=[]


    print("\nNow, please enter {n} rows, each containing {m} integers separated by spaces.")
    print("Example: For a row with 3 columns, you would enter something like '1 2 3' each time when asked.\n")


    for i in range (n):
        while True:
            row = input("enter a single row with m no.of space-separated integers: ").split()
            if len(row) != m:
                 print(f"Error: You must enter exactly {m} integers for the row. Please try again.")
            else:
                break 
        r = [int(x) for x in row]
        mat.append(r)
    r1=[]
    r2=[]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
               r1.append(i)
               r2.append(j)
            
    for i in range(n):
         for j in range(m):
             if i in r1 or j in r2:
                 mat[i][j] = 0

    print("\nThe modified matrix is")            
    for r in mat:
        for m in r:
          print(m,end=" ")
        print()
    ans=input("\nPress 'Y' or 'y' to continue, otherwise press any key to exit:\n" )
    
    




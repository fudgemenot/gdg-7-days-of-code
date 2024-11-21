ans="y"
print("X : Number of schools;Y: Number of students in each school;Z: Number of students who passed the exams")
while ans.lower()=="y":
    def testcases():
         list1= input("Enter x y z digits for testcase 1: ").split()  
         list2= input("Enter x y z digits for testcase 2: ").split()
         list3= input("Enter x y z digits for testcase 3: ").split()
         l1 = [int(x) for x in list1]
         l2 = [int(x) for x in list2]
         l3 = [int(x) for x in list3]
         return l1, l2, l3
        
    l1, l2, l3 = testcases()
    
    def calc(a):
       return (a[2] / (a[0] * a[1])) * 100

    r=[]
    r.append(calc(l1))
    r.append(calc(l2))
    r.append(calc(l3))

    for i in r:
       if i>50:
         print("YES")
       else:
        print("NO")
        
    ans=input("Press 'Y' or 'y' to continue, otherwise press any key to exit:" )

n=int(input("enter the number:"))
factorial=1
if(n<0):
    print("negetive value cannot done:")
elif(n==0):
    print("the factorial number 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
        print("the factorial number is:",factorial)

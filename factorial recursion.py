def factorial(n):
    if(n==1):
        return n
    else:
        return (n*factorial(n-1))
n=int(input("enter the number:"))
if(n<0):
    print("please enter positive value")
elif(n==0):
    print("the fsctorial of 0 is 1")
else:
    print("the factorial number is:",factorial(n))

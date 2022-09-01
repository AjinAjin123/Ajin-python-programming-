print("Enter The nth Prime Number:")
x=int(input())
n,c=1,0
while(c<x):
    n+=1
    for i in range(2,n+1):
        if(n%i==0):
            break
    if(i==n):
        c=c+1
print("the nth prime number is:",n)

print("Prime numbers after nth term:",end=' ')
numr=n+10
for t in range(n,numr):

    for i in range(2,t):

        if(t%i==0):

            break

    else:

        print(t,end=' ')     

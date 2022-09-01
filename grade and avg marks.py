import math as M
c=float(input("enter the mark:"))
sql=float(input("enter the mark:"))
python=float(input("enter the mark:"))
java=float(input("enter the mark:"))
sum=c+sql+python+java
avg=sum/4
print("sum",sum)
print("average",avg)
if(avg>=90):
    print("grade S")
elif(avg>=80):
    print("grade A")
elif(avg>=70):
    print("grade B")
elif(avg>=60):
    print("grade C")
else:
    print("FAIL")
    


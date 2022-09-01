print("enter the 5 subject marks")
english=float(input("enter the marks:"))
maths=float(input("enter the marks:"))
python=float(input("enter the marks:"))
physics=float(input("enter the marks:"))
c=float(input("enter the marks:"))
sum=english+maths+python+physics+c
avg=sum/5
print("average,sum",avg,sum ,end=" ")
if(avg>=90):
    print("grade A")
elif(avg>=80):
    print("grade B")
elif(avg>=70):
    print("grade C")
elif(avg>=60):
    print("grade D")
else:
    print("fail")



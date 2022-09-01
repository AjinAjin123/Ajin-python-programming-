import math as M
number1=float(input("enter the number1:"))
number2=float(input("enter the number2:"))
number3=float(input("enter the number3:"))
if(number1>number2)and(number1<number2):
    greatest=number1
elif(number2>number1)and(number2>number3):
    greatest=number2
else:
    greatest=number3
print("the greatest number is:",greatest)

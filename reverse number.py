print("enter the numbers:")
numone=int(input())
numtwo=int(input())
numthree=int(input())
if numone<numtwo and numone<numthree:
    print(numone,"is the greatest number")
elif numtwo<numone and numtwo<numthree:
    print(numtwo,"is the greatest number")
else:
    print(numthree,"is the greatest number")

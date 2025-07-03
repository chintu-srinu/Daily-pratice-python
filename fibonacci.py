num1,num2=0,1
for i in range(0,5):
    temp=num1+num2
    num1=num2
    num2=temp
print(temp)

n=9
num1,num2=0,1
count=0
while count<n:
    temp=num1+num2
    num1=num2
    num2=temp
    count+=1
print(temp)

n=20
num1,num2=0,1
count=0
while count<n:
    temp=num1+num2
    num1=num2
    num2=temp
    count+=1
print(temp)

num=int(input("enter a number"))
num1,num2=0,1
while num1 <num:
    temp=num1+num2
    num1=num2
    num2=temp
if num1==num:
    print("fib")
else:
    print("no")

def recursion(num):
    if num<=1:
        return num
    else:
        return recursion (num-1)+recursion(num-2)
n=10
for i in range(n):
    print(recursion(i),end=" ")

n = int(input("Enter number of terms: "))
num1,num2=0,1
fib=[num1,num2]
for i in range(2,n):
    temp=num1+num2
    fib.append(temp)
    num1=num2
    num2=temp
for i in range(len(fib)-1,-1,-1):
    print(fib[i],end=" ")




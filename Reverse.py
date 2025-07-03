# //reverse
num=1213
temp=num
rev_num=0
while temp>0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
print(rev_num)

num=int(input("enter a number"))
def reverse (input_num):
    temp=input_num
    rev_num=0
    while temp >0:
        rem=temp%10
        rev_num=rev_num*10+rem
        temp//=10
    return rev_num
res=reverse(num)
print(res)

# //palindorme
num=121
temp=num
rev_num=0
while temp>0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
if num==rev_num:
    print("palindrome")
else:
    print("not")
    
num=int(input("enter a number"))
def reverse (input_num):
    temp=input_num
    rev_num=0
    while temp >0:
        rem=temp%10
        rev_num=rev_num*10+rem
        temp//=10
    return rev_num
res=reverse(121)
if num==res:
    print("palin")
else:
    print("no")
    
#  //recursion  
def recursion(num,rev=0):
    if num==0:
        return rev
    else:
        return recursion(num//10,rev*10+num%10)
num=123
res=recursion(num)
print(res)

# spaces between numbers
num=int(input("enter a number"))
temp=num
# rev_num=0
while temp>0:
    rem=temp%10
    print(rem,end=" ")
    # rev_num=rev_num*10+rem
    temp//=10
print(temp)

#divsible
num=int(input("enter a number"))
temp=num
rev_num=0
while temp>0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
print(rev_num)
if num%7==0:
    print("divisble")
else:
    print("no")

num=int(input("enter a number"))
def reverse(input_num):
    temp=input_num
    rev_num=0
    while temp>0:
        rem=temp%10
        rev_num=rev_num*10+rem
        temp//=10
    return rev_num
res=reverse(num)
print(res)
if num%7==0:
    print("yes")
else:
    print("no")

# without zeros(0)
num=1200
temp=num
rev_num=0
while temp>0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
print(rev_num)

#reverse
num=int(input("enter a number"))
def reverse(input_num):
    temp=input_num
    rev_num=0
    while temp>0:
        rem=temp%10
        rev_num=rev_num*10+rem
        temp//=10
    return rev_num
res=reverse(num)
print(res)

#greater or lesser
num=123
temp=num
rev_num=0
while temp>0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
print(rev_num)
if num >rev_num:
    print("the num is greater",num)
    print(rev_num)
else:
    print("the rev_num is greater",rev_num)
    print(num)

#differnce of rev_num and num
num=int(input("enter a number"))
temp=num
rev_num=0
while temp >0:
    rem=temp%10
    rev_num=rev_num*10+rem
    temp//=10
diff=abs(num-rev_num)
print(rev_num)
print(diff)

#count the palin
num=[101,343,232,585,987,98,989]
count=0
for i in num:
    if str(i)==str(i)[::-1]:
        count+=1
print("palin",count)
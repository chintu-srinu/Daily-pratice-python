num=int(input("enter a number"))
temp=num
sum=0
while temp >0:
    rem=temp%10
    sum+=rem**3
    temp//=10
if sum==num:
    print("yes armstrong")
else:
    print("not an amstrong")
 
    
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum+=rem**len(str(num))
    temp//=10
if sum==num:
    print("yes armstrong")
else:
    print("not an amstrong")
   
    
num=int(input("enter a number"))
temp2=num
count=0
while temp2>0:
    count+=1
    temp2//=10
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum+=rem**count
    temp//=10
if sum==num:
    print("yes armstrong")
else:
    print("not an amstrong")


num=int(input("enter a number"))
temp=num
sum=0
for i in range(0,1000):
    rem=temp%10
    sum+=rem**len(str(num))
    temp//=10
if sum==num:
        print("yes armstrong")
else:
    print("not an amstrong")

count = 0

for num in range(1, 1001):
    temp2 = num
    digit_count = 0

    while temp2 > 0:
        digit_count += 1
        temp2 //= 10

    temp = num
    armstrong_sum = 0
    
    while temp > 0:
        rem = temp % 10
        armstrong_sum += rem ** digit_count
        temp //= 10

    if armstrong_sum == num:
        count += 1

print("Total Armstrong numbers between 1 and 1000:", count)




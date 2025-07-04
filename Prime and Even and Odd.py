#PRIME NUMBER

def check_prime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
    return True
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    fun_res=check_prime(rem)
    if fun_res==True:
        sum+=rem
    temp//=10
print(sum)

#EVEN NUMBER

num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    if rem%2==0:
        sum+=rem
    temp//=10
print(sum)

#PALINDROME

num=int(input("enter a number"))
def palindrome(input_num):
    temp=input_num
    rev_num=0
    while temp>0:
        rem=temp%10
        rev_num=rev_num*10+rem
        temp//=10
    return rev_num
if num==palindrome(num):
    print("palindrome")
else:
    print("not a palindrome")

#STRING PALINDROME

text=input("enter a string")
def palindrome(input_num):
    temp=input_num
    rev_str=""
    index=len(temp)-1
    while index>=0:
        rev_str+=temp[index]
        index-=1
    return rev_str
if text==palindrome(text):
    print("palindrome")
else:
    print("not a palindrome")

#SUM OF PRIME

def prime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
    return True
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    fun_res=prime(rem)
    if fun_res==True:
        sum+=rem
    temp//=10
print(sum)

#SUM OF NON_PRIME

def non_prime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
    return True
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    fun_res=non_prime(rem)
    if fun_res==False:
        sum+=rem
    temp//=10
print(sum)

#PRODUCT OF NON_PRIME

def non_prime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
    return True
num=int(input("enter a number"))
temp=num
sum=1
found=False
while temp >0:
    rem=temp%10
    fun_res=non_prime(rem)
    if fun_res==False:
        sum*=rem
        found=True
    temp//=10
if found:
    print(sum)
else:
    print("all are non prime digits")

#SUM OF PRIME

def prime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
    return True
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    fun_res=prime(rem)
    if fun_res==True:
        sum+=rem
    temp//=10
if num==sum:
    print("prime")
else:
    print("not a prime")

#SUM OF NON_PRIME

def sum_nonprime(input_num):
    if input_num<=1:
        return False
    for i in range(2,input_num):
        if input_num%i==0:
            return False
        return True
num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    fun_res=sum_nonprime(rem)
    if fun_res==False:
        sum+=rem
    temp//=10
print(sum)

#SUM OF EVEN

num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    rem=temp%10
    if rem%2==0:
        sum+=rem
    temp//=10
print(sum)

#SUM OF ODD

num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    if rem%2==1:
        sum+=rem
    temp//=10
print(sum)

# DIFF OF EVEN AND ODD

num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    if rem %2==0:
        sum+=rem
    temp//=10
num1=int(input("enter a number"))
temp=num
sum1=0
while temp>0:
    rem=temp%10
    if rem%2==1:
        sum1+=rem
    temp//=10
diff=abs(num-num1)
print(sum)
print(sum1)
print(diff)

# SUM OF EVEN AND PRIME

def prime(input_num):
    if input_num <= 1:
        return False
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
    return True
num = int(input("Enter first number (for prime digit sum): "))
temp = num
sum = 0

while temp > 0:
    rem = temp % 10
    if prime(rem):
        sum += rem
    temp //= 10
num = int(input("Enter second number (for even digit sum): "))
temp = num
sum1 = 0

while temp > 0:
    rem = temp % 10
    if rem % 2 == 0:
        sum1 += rem
    temp //= 10

digits_sum = set(str(sum))
digits_sum1 = set(str(sum1))
common_digits = digits_sum & digits_sum1

if common_digits:
    print("Common digits:", ", ".join(sorted(common_digits)))
else:
    print("No common digits found.")

    
    
    
    
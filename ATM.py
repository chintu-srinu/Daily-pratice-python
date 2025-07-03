db_username="chintu"
db_password="123"
total_remain_chances=3
while total_remain_chances>0:
    input_user=input("enter username")
    input_password=input("enter password")
    if db_username==input_user and db_password ==input_password:
        print("login")
        break
        total_remain_chances=0
    else:
        total_remain_chances -=1
        print("relogin")
        print("total remaining chances",total_remain_chances)
        if total_remain_chances <=0:
            print(total_remain_chances,"chances chances completed login after 24hrs")
            
            
num=(input("please enter atm card (yes/no):"))
button=True
balance=5000
available_cash=[500,1000,2000]
if num=="yes" and button:
    print("available notes",available_cash)
    amount=int(input("enter amout"))
    if amount >balance:
        print("insufficient")
    elif amount < 500:
        print("no available cash only this is  cash is available" ,available_cash)
    else:
        print("seccesfully withdrawn ",amount)
        balance-=amount
        print("take your recicept",)
        print("remaing balance in your account is",balance)
else:
    print("cancelled withdrwal")

num=(input("please enter atm card (yes/no):"))
button=True
balance=5000
available_cash=[500,1000,2000]
if num=="yes" and button:
    print("available notes",available_cash)
    amount=int(input("enter amout"))
    if amount in available_cash:
        if amount <= balance:
            # amount=int(input("enter amout"))
            print("seccesfully withdrawn ",amount)
            balance-=amount
            print("take your recicept",)
            print("remaing balance in your account is",balance)
        elif amount >balance:
            print("insufficient")
    else:
        print("no available cash only this  cash is available" ,available_cash)
else:
    print("cancelled withdrwal")
    

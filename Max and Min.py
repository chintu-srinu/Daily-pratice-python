#3 MAX AND MIN NUMBERS

list=[1,2,3,4,5,6]
min_num=list[0]
max_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if  i >max_num:
        max_num=i
print(min_num)
print(max_num)

second_min=max_num
second_max=min_num
for i in list:
    if min_num < i<second_min:
        second_min=i
    if max_num > i >second_max:
        second_max=i
print(second_min)
print(second_max)

third_max=min_num
third_min=max_num
for i in list:
    if i!=min_num and i!=second_min and i<third_min:
        third_min=i
    if i!=max_num and i!=second_max and i>third_max:
        third_max=i
print(third_max)
print(third_min)

#Second Maximum

list=[ 5,9,2,6,3]
max_num=list[0]
min_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if i >max_num:
        max_num=i
second_max=min_num
for i in list:
    if max_num>i>second_max:
        second_max=i
print(second_max)

# Third Minimum

list=[1,2,3,4,5,6]
max_num=list[0]
min_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if i >max_num:
        max_num=i
second_max=min_num
second_min=max_num
for i in list:
    if min_num<i<second_min:
        second_min=i
    if max_num>i>second_max:
        second_max=i
# print(second_max)

third_min=max_num
for i in list:
    if min_num<second_min<i<third_min:
        third_min=i
print(third_min)

# First, Second, and Third Maximum

list=[1,2,3,4,5,6,7]
max_num=list[0]
min_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if i >max_num:
        max_num=i
print(max_num)
second_max=min_num
second_min=max_num
for i in list:
    if min_num<i<second_min:
        second_min=i
    if max_num>i>second_max:
        second_max=i
print(second_max)

third_min=max_num
third_max=min_num
for i in list:
    if min_num<second_min<i<third_min:
        third_min=i
    if max_num>second_max>i>third_max:
        third_max=i
print(third_max)

# First and Second Smallest 

list=[1,2,3,4,5,6,7]
max_num=list[0]
min_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if i >max_num:
        max_num=i
print(min_num)
second_max=min_num
second_min=max_num
for i in list:
    if min_num<i<second_min:
        second_min=i
print(second_min)

#  First Max and Last Min
list=[1,2,3,4,5]
min_num=list[0]
max_num=list[0]
for i in list:
    if i<min_num:
        min_num=i
    if  i >max_num:
        max_num=i

second_min=max_num
second_max=min_num
for i in list:
    if min_num < i<second_min:
        second_min=i
    if max_num > i >second_max:
        second_max=i

third_max=min_num
third_min=max_num
for i in list:
    if i!=min_num and i!=second_min and i<third_min:
        third_min=i
    if i!=max_num and i!=second_max and i>third_max:
        third_max=i

if max_num>third_min:
    print(max_num)
else: 
    print(third_min)



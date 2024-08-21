# تعریف چندین لیست از اعداد
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

# محاسبه مجموع و میانگین برای list1
sum1 = 0
for num in list1:
    sum1 += num
average1 = sum1 / len(list1)
print("Sum of list1:", sum1)
print("Average of list1:", average1)

# محاسبه مجموع و میانگین برای list2
sum2 = 0
for num in list2:
    sum2 += num
average2 = sum2 / len(list2)
print("Sum of list2:", sum2)
print("Average of list2:", average2)

# محاسبه مجموع و میانگین برای list3
sum3 = 0
for num in list3:
    sum3 += num
average3 = sum3 / len(list3)
print("Sum of list3:", sum3)
print("Average of list3:", average3)

# پیدا کردن بیشترین و کمترین مقدار در list1
max1 = list1[0]
min1 = list1[0]
for num in list1:
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num
print("Max of list1:", max1)
print("Min of list1:", min1)

# پیدا کردن بیشترین و کمترین مقدار در list2
max2 = list2[0]
min2 = list2[0]
for num in list2:
    if num > max2:
        max2 = num
    if num < min2:
        min2 = num
print("Max of list2:", max2)
print("Min of list2:", min2)

# پیدا کردن بیشترین و کمترین مقدار در list3
max3 = list3[0]
min3 = list3[0]
for num in list3:
    if num > max3:
        max3 = num
    if num < min3:
        min3 = num
print("Max of list3:", max3)
print("Min of list3:", min3)



# بررسی اینکه آیا عدد خاصی در لیست‌ها وجود دارد یا خیر
target = 250
found_in_list1 = False
for num in list1:
    if num == target:
        found_in_list1 = True
        break
if found_in_list1:
    print(f"{target} found in list1")
else:
    print(f"{target} not found in list1")

found_in_list2 = False
for num in list2:
    if num == target:
        found_in_list2 = True
        break
if found_in_list2:
    print(f"{target} found in list2")
else:
    print(f"{target} not found in list2")

found_in_list3 = False
for num in list3:
    if num == target:
        found_in_list3 = True
        break
if found_in_list3:
    print(f"{target} found in list3")
else:
    print(f"{target} not found in list3")

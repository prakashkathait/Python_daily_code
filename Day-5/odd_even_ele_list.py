#Exercise 10: Create a new list from two list using the following condition

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for ele in list1:
    if ele %2!=0:
        list3.append(ele)
for ele2 in list2:
    if ele2 %2 ==0:
        list3.append(ele2)
print(list3)
list1 = [0.1,90,2,8,3,700,4,6,500,0.001]

list1_min = list1[0]
list1_max = list1[0]

for i in range(len(list1)):
    if list1_min > list1[i]:
        list1_min = list1[i]
        min_indices = i
    elif list1_max < list1[i]:
        list1_max = list1[i]
        max_indices = i
print(list1_min,list1_max,max_indices,min_indices)

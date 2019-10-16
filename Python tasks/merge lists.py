list1 = [2, 5, 15, 36, 47, 56, 59, 78, 156, 244, 268]
list2 = [18, 39, 42, 43, 66, 69, 100]
mergelist = []
i = 0
j = 0
while (i < len(list1)) and (j < len(list2)):
    if list1[i] < list2[j]:
        mergelist.append(list1[i])
        i += 1
    else:
        mergelist.append(list2[j])
        j += 1
while (i < len(list1)):
    mergelist.append(list1[i])
    i += 1
while (j < len(list2)):
    mergelist.append(list2[j])
    j += 1
print(list1, list2, mergelist)

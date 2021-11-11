list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list = []
i = 0
while i<len(list1):
    j = list1[i]
    if j not in list2:
        list.append(j)
    i+=1
print(list)





ist1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list = []
i = 0 
while i < len(list2):
    if list1[i] not in list2:
        list.append(list1[i])
    i+=1
print(list)

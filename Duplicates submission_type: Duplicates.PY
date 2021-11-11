n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
list=[]
i=0
while i<len(n):
    if n[i] not in list:
        list.append(n[i])
    i+=1
print(list)




n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
list=[]
for i in n:
    if i not in list:
        list.append(i)
print(list)



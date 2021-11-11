number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
list1=[]
while i < len(n):
    j=0
    while j<i:
        if n[j]+n[i]==number:
            list1.append([n[i],n[j]])
        j+=1
    i+=1
print(list1)
    


    
    
while i < len(n):
    if i == 4:
        break
    j = 0 
    while j< len(n):
        if n[i]+n[j]==number:
            c = [n[i],n[j]]
            list1.append(c)
        j+=1
    i+=1
print(list1)

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count = 0
count1 = 0
sum=0
sum1=0
while i < len(elements):
    if elements[i]%2==0:
        count+=1
        sum = sum + elements[i]
        average = sum / count
    else:
        count1+=1
        sum1 = sum1 + elements[i]
        avg = sum1 / count1
    i+=1
print("even numbers sum:",sum ,"\n","average of even numbers:",average)
print("odd numbers sum:",sum1 ,"\n","average of odd numbers:",avg)



# i=0
# sum=0
# sum1=0
# while i<len(elements):
#     if elements[i]%2==0:
#         list1.append(elements[i])
#         print(elements[i],"=","EVEN")
#         sum=sum+ elements[i]
#         avg=sum/len(elements)
#     else:
#         list2.append(elements[i])
#         print(elements[i],"=","ODD")
#         sum1=sum1+elements[i]
#         avg=sum1/len(elements)
#     i+=1
# print("sum1 =",sum)
# print("avg =",avg)
